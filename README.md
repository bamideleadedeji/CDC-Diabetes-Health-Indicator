# CDC Diabetes Health Indicators Analysis & Risk Assessment Tool

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-red)
![License](https://img.shields.io/badge/license-MIT-green)
![Data](https://img.shields.io/badge/dataset-253,680%20samples-orange)

## Project Overview

This project analyzes lifestyle factors affecting diabetes risk in the USA using CDC's Behavioral Risk Factor Surveillance System (BRFSS) data. The dataset includes health indicators from 253,680 Americans with 21 features related to lifestyle, demographics, and health conditions.

**Key Findings:**
- **BMI is the strongest predictor** of diabetes risk
- **Physical activity** significantly reduces diabetes risk
- **Class imbalance** (85% no diabetes, 15% diabetes/pre-diabetes) requires special handling
- **Self-reported health** is surprisingly accurate in predicting diabetes

## Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app/)

## Project Structure
diabetes-cdc-analysis/
├── notebooks/ # Jupyter notebooks for analysis
│ ├── 01_eda_analysis.ipynb # Exploratory Data Analysis
│ ├── 02_model_building.ipynb # Machine Learning Models
│ └── 03_feature_analysis.ipynb # Feature Importance
├── streamlit_app/ # Web application
│ ├── app.py # Main Streamlit application
│ ├── components/ # Reusable components
│ ├── assets/ # Images, CSS, etc.
│ └── config.toml # Streamlit configuration
├── src/ # Source code
│ ├── data_loader.py # Data loading utilities
│ ├── preprocessing.py # Data preprocessing
│ └── models.py # ML model definitions
├── tests/ # Unit tests
├── docs/ # Documentation
├── data/ # Data directory
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore file
├── LICENSE # MIT License
├── README.md # This file
└── executive_summary.md # Detailed project summary


## Installation

### Localal Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/bamideleadedeji/diabetes-cdc-analysis.git
   cd diabetes-cdc-analysis
