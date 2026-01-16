
## End-to-End Machine Learning Project for Student Performance Prediction

## 📌 Project Overview
This project demonstrates a **production-grade, end-to-end Machine Learning pipeline** built using real-world industry best practices.  
The objective is to **predict students’ math scores** based on demographic and academic features while ensuring **reproducibility, scalability, and maintainability**.

The project covers the complete ML lifecycle:
- Project setup & automation
- SQL-based data ingestion
- Data versioning
- Feature engineering
- Model training & hyperparameter tuning
- Experiment tracking
- Logging & exception handling

---

## 🎯 Problem Statement
Educational institutions often lack early insights into factors affecting student performance.  
This project predicts **math scores** using student-related attributes to enable **data-driven academic decisions**.

---

## ⚙️ Tech Stack
- **Programming Language:** Python  
- **Data Processing:** Pandas, NumPy  
- **Machine Learning:** Scikit-learn, XGBoost, CatBoost  
- **Database:** MySQL  
- **Experiment Tracking:** MLflow, DagsHub  
- **Data Versioning:** DVC  
- **Version Control:** Git & GitHub  
- **Environment Management:** Conda / Virtual Environment  

---

## 🔄 End-to-End Workflow

### 1️⃣ Project Setup & Automation
- Initialized Git repository with proper `.gitignore`
- Created reusable project structure using Python templating & Cookiecutter
- Packaged project using `setup.py`
- Managed dependencies via `requirements.txt`

---

### 2️⃣ Data Ingestion
- Read data directly from **MySQL database**
- Stored credentials securely using environment variables
- Saved raw, train, and test datasets in `artifacts/`
- Performed **80–20 train-test split**

---

### 3️⃣ Data Versioning (DVC)
- Tracked large datasets using **DVC**
- Synced dataset versions with Git commits
- Enabled rollback to previous data versions using:


---

### 4️⃣ Exploratory Data Analysis (EDA)
- Identified numerical & categorical features
- Created derived feature: **average score**
- Key insights:
- Standard lunch improves performance
- Test preparation boosts scores
- Female students show slightly higher averages

---

### 5️⃣ Data Transformation
- Implemented Scikit-learn pipelines:
- Missing value imputation
- One-Hot Encoding
- Feature scaling
- Used **ColumnTransformer**
- Saved preprocessing pipeline as `preprocessor.pkl`

---

### 6️⃣ Model Training & Hyperparameter Tuning
- Trained multiple regression models:
- Linear Regression
- Ridge & Lasso
- Decision Tree
- Random Forest
- AdaBoost
- Gradient Boosting
- XGBoost
- CatBoost
- Used **GridSearchCV** for tuning
- Selected best model using **R² score**
- Final model achieved **~87% R²**
- Saved model as `model.pkl`

---

### 7️⃣ Experiment Tracking (MLflow + DagsHub)
- Logged parameters and metrics using MLflow
- Tracked experiments on **DagsHub**
- Compared multiple runs via UI

MLFLOW_TRACKING_URI=https://dagshub.com/bjbcr7/DSproject.mlflow \
MLFLOW_TRACKING_USERNAME=bjbcr7 \
MLFLOW_TRACKING_PASSWORD=6cad94e022ee5401b0b31cf0127477fe76f6f260 \
python script.py

---

### 8️⃣ Logging & Exception Handling
- Implemented timestamp-based logging
- Created custom exception handling capturing:
- Error message
- File name
- Line number
- Improved debuggability & production readiness

---

## 📊 Results
- **Best Model R² Score:** ~85%
- Strong generalization between train & test data
- Minimal overfitting

---





