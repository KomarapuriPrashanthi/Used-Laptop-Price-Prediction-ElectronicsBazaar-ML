# 💻 Used Laptop Price Prediction (ElectronicsBazaar) - ML

## 📌 Project Overview
This project predicts the price of second-hand laptops using Machine Learning techniques.  
The dataset was scraped from ElectronicsBazaar and processed for model training and evaluation.

The workflow includes:
- Web scraping using Selenium
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Model training and comparison
- Final price prediction using the best model

---

## 📂 Project Structure

Used-Laptop-Price-Prediction-ElectronicsBazaar-ML/
│
├── data/
│   ├── raw_laptop_data.csv
│   ├── cleaned_laptop_data.csv
│   └── predicted_prices.csv
│
├── scraping/
│   └── scrape_laptop_data.py
│
├── preprocessing/
│   └── data_preprocessing.py
│
├── EDA.ipynb
├── ML_Model.ipynb
├── requirements.txt
└── README.md

---

## 🔍 Exploratory Data Analysis
EDA includes:
- Dataset overview
- Missing value analysis
- Correlation heatmap
- Statistical summaries

---

## 🤖 Machine Learning Models Used

The following regression models were trained and evaluated:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- Support Vector Regressor
- XGBoost Regressor

The best performing model (based on MAE and R² score) was selected and saved using `joblib`.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Seaborn
- Matplotlib
- Selenium

---

## 📈 Output

The trained model predicts laptop prices and saves results in:
data/predicted_prices.csv

---

## 📌 Conclusion

This project demonstrates an end-to-end Machine Learning pipeline:
Data Collection → Data Cleaning → EDA → Model Training → Prediction.
