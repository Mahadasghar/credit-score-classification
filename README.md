# Credit Score Classification 📊

A clean, reproducible machine learning project for **Credit Score Classification** using **Logistic Regression** and **Random Forest**.  
The notebook covers the full ML workflow: data preprocessing, exploratory data analysis (EDA), model training, hyperparameter tuning, and evaluation with performance metrics.

---

## 🚀 Features
- Preprocessing pipeline with missing value handling and encoding  
- Logistic Regression and Random Forest classifiers  
- Cross-validation for robust evaluation  
- Performance metrics: Accuracy, Classification Report, Confusion Matrix  
- Well-documented Jupyter Notebook with step-by-step explanations  

---

## 📂 Project Structure
```bash
credit-score-classification/
│── classifier.ipynb                 # Main Jupyter Notebook
│── credit_score_classification.csv  # Dataset used in the project
│── requirements.txt                 # Dependencies
│── README.md                        # Project documentation
│── LICENSE                          # MIT License
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

📊 Results

Logistic Regression and Random Forest classifiers were trained and evaluated.

Performance metrics (accuracy, precision, recall, F1-score) and confusion matrix are provided.

Random Forest showed slightly better results due to handling feature interactions.
