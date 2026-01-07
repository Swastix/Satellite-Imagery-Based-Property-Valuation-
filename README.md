# Satellite Imagery-Based Property Valuation

## Project Overview
This project develops a **Multimodal Regression Pipeline** to predict residential property values.  
It integrates traditional **tabular features** (e.g., square footage, grade, location) with **high-dimensional visual embeddings** extracted from satellite imagery via the **MAPBOX API**.

The core objective is to evaluate whether **environmental context**—such as greenery, neighborhood density, and road infrastructure—provides a measurable predictive lift over standard structural attributes alone.

---

### 📥 Cloning the Repository

First, clone the project repository to your local machine.

```bash
git clone https://github.com/<your-username>/<your-repository-name>.git
```

Navigate into the project directory:

```bash
cd <your-repository-name>
```

---

After cloning the repository, proceed with setting up the virtual environment as described below.

### Environment Setup & Installation

This project is implemented in Python and uses a combination of tabular machine learning models, neural networks, and satellite imagery.
It is recommended to run all experiments inside a **virtual environment**

---

#### 🐍 Creating a Virtual Environment

##### Windows (PowerShell)

```powershell
python -m venv venv
```

##### macOS / Linux

```bash
python3 -m venv venv
```

---

#### ▶ Activating the Virtual Environment

##### Windows

```powershell
venv\Scripts\activate
```

##### macOS / Linux

```bash
source venv/bin/activate
```

Once activated, your terminal should show `(venv)`.

---

### 📥 Installing Dependencies

Upgrade `pip` and install all required packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

#### 🔐 Environment Variables

This project uses a `.env` file to manage sensitive configuration.

An empty `.env` file is included in the repository as a **template**.

##### Required variables

Edit the `.env` file and add:

```env
MAPBOX_API_KEY=your_mapbox_access_token_here
```

⚠️ **Do not commit your API key.**
The `.env` file should remain empty in version control and populated only in your local environment.

The environment variables are loaded at runtime using `python-dotenv`.

---

### 🛰️ Data Acquisition (Satellite Imagery)

Satellite images are downloaded using the Mapbox Static Images API based on property latitude and longitude.

To download images:

```bash
python data_fetcher.py
```

This script:

* Reads coordinates from `train.csv`
* Downloads satellite images at multiple zoom levels
* Stores images locally for downstream feature extraction

---

Here is a **clean, professional, README-ready description** for both notebooks.
You can **copy-paste this directly** under your *Code Repository* section.

---

### 📓 `preprocessing.ipynb`

This notebook contains the **exploratory analysis, preprocessing, and feature engineering pipeline** used in the project.

Key components include:

* **Exploratory Data Analysis (EDA)** of the housing dataset to understand feature distributions, correlations, and price drivers.
* **Data cleaning and preprocessing**, including handling categorical variables, feature transformations, and target log-scaling.
* **Baseline tabular modeling**, where multiple tabular regression models (e.g., CatBoost) are trained and evaluated to establish strong non-image baselines.
* **Image feature extraction** using pretrained convolutional neural networks to generate fixed-length embedding vectors from satellite imagery.
* **Model interpretability via Grad-CAM**, highlighting spatial regions in satellite images that contribute most to model predictions.

This notebook serves as the **foundation of the project**, and the results and visualizations generated here are **referenced and discussed in the final report**.

---

### 📓 `model_training.ipynb`

This notebook focuses on **multimodal model experimentation and evaluation**, combining both **tabular and image-based features**.

Key components include:

* **Construction and evaluation of multimodal architectures** that fuse satellite image embeddings with tabular property features.
* **Comparison of multiple fusion strategies**, including early fusion, late fusion, and stacked meta-learning approaches.
* **Neural network–based image regressors** trained on extracted embeddings and combined with tabular predictions.
* **Performance analysis** comparing tabular-only, image-only, and multimodal models to quantify the contribution of visual information.
* **Final model selection and validation**, with metrics reported in both log-price and original price space.

This notebook represents the **core experimental phase** of the project and contains the implementations and results used to draw the **final conclusions** about the effectiveness of multimodal learning for property price prediction.

---

### Final Deliverables
- **`23321030_final.csv`**  
  Final output file containing predicted property prices for the test dataset.

- **`23321030_report.pdf`**  
  Complete project documentation including:
  - Overview 
  - EDA
  - Financial / Visual Insight
  - Architecture Diagram
  - Results


---
Swastik Panda 23321030
BS-MS Economics  
Indian Institute of Technology Roorkee
