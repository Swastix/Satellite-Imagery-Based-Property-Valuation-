"""
data_fetcher.py

Downloads satellite images for properties using latitude/longitude
coordinates via the Mapbox Static Images API.

Requirements:
- MAPBOX_API_KEY set as an environment variable
- train.csv containing 'lat' and 'long' columns
"""

from dotenv import load_dotenv
import os

load_dotenv()  # loads variables from .env into environment

MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY")

if MAPBOX_API_KEY is None:
    raise RuntimeError("MAPBOX_API_KEY not found in .env file")


import os
import time
import requests
import pandas as pd
from pathlib import Path
from tqdm.auto import tqdm
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# ============================================================
# Configuration
# ============================================================

CSV_PATH = "train.csv"
IMAGE_DIR = Path("images")
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

ZOOMS = [16, 17, 18]
IMAGE_SIZE = "224x224"
RATE_LIMIT_SLEEP = 0.2

MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY")
if MAPBOX_API_KEY is None:
    raise RuntimeError(
        "MAPBOX_API_KEY not found. "
        "Please set it as an environment variable."
    )


# ============================================================
# HTTP Session with retries
# ============================================================

def create_session():
    session = requests.Session()

    retries = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
    )

    adapter = HTTPAdapter(max_retries=retries)
    session.mount("https://", adapter)

    return session


# ============================================================
# Image download logic
# ============================================================

def download_multi_zoom(session, lat, lon, base_path):
    for z in ZOOMS:
        save_path = base_path.with_suffix(f".z{z}.png")

        if save_path.exists():
            continue

        url = (
            "https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/"
            f"{lon},{lat},{z}/{IMAGE_SIZE}"
            f"?access_token={MAPBOX_API_KEY}"
        )

        try:
            r = session.get(url, timeout=10)
            r.raise_for_status()
            save_path.write_bytes(r.content)

        except Exception as e:
            print(f"[WARN] Failed {save_path.name}: {e}")


# ============================================================
# Main execution
# ============================================================

def main():
    df = pd.read_csv(CSV_PATH)

    if not {"lat", "long"}.issubset(df.columns):
        raise ValueError("CSV must contain 'lat' and 'long' columns")

    session = create_session()

    for i, row in tqdm(
        df.iterrows(),
        total=len(df),
        desc="Downloading satellite images"
    ):
        lat = row["lat"]
        lon = row["long"]

        base_path = IMAGE_DIR / str(i)
        download_multi_zoom(session, lat, lon, base_path)

        time.sleep(RATE_LIMIT_SLEEP)


# ============================================================
# Entry point
# ============================================================

if __name__ == "__main__":
    main()
