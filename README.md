# Credit Score Classification 📊

A clean, reproducible machine learning project for **Credit Score Classification** using **Logistic Regression** and **Random Forest**.  
The notebook covers the full ML workflow: data preprocessing, exploratory data analysis (EDA), model training, hyperparameter tuning, evaluation with performance metrics, and a simple **Streamlit web app** for interactive predictions.

---

## 🚀 Features
- Preprocessing pipeline with missing value handling and encoding  
- Logistic Regression and Random Forest classifiers  
- Cross-validation for robust evaluation  
- Performance metrics: Accuracy, Classification Report, Confusion Matrix, ROC-AUC  
- Well-documented Jupyter Notebook with step-by-step explanations  
- Interactive **Streamlit app** to test predictions with custom inputs  

---

## 📂 Project Structure
```bash
credit-score-classification/
│── classifier.ipynb                 # Main Jupyter Notebook
│── credit_score_classification.csv  # Dataset used in the project
│── requirements.txt                 # Dependencies
│── README.md                        # Project documentation
│── LICENSE                          # MIT License
│── app.py                           # Streamlit app for predictions
│── best_credit_score_model.pkl      # Saved ML pipeline (pickle format)
```

📊 Dataset

The dataset used in this project is provided in the repository:
credit_score_classification.csv

Contains features related to individuals’ financial/credit history

Target variable: Credit Score Category (e.g., Good / Bad)

Used for training and evaluating classification models

⚙️ Installation

Clone the repository and install dependencies:
```bash

git clone https://github.com/Mahadasghar/credit-score-classification.git
cd credit-score-classification
pip install -r requirements.txt
```
▶️ Usage
1. Run Jupyter Notebook

To explore the full workflow:
```bash

Jupyter Notebook classifier.ipynb
```
2. Run the Streamlit App

Launch the interactive prediction app:
```bash
streamlit run app.py
```

This will open a browser window where you can input features such as Age, Income, Gender, Education, Marital Status, Number of Children, and Home Ownership to get a predicted Credit Score Category along with a confidence score.

📊 Results

Logistic Regression and Random Forest classifiers were trained and evaluated.

Performance metrics (accuracy, precision, recall, F1-score, ROC-AUC) and a confusion matrix are provided in the notebook.

Random Forest showed slightly better results due to its ability to handle feature interactions.

The Streamlit app enables real-time credit score classification with user-friendly input fields.
