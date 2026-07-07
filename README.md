# 📊 Telco Customer Churn Prediction - End-to-End Pipeline

## 🎯 Project Overview
This project is an end-to-end data pipeline and machine learning model designed to predict customer churn in the telecom industry. 
It demonstrates the integration of Data Engineering (ETL) and Data Science (Machine Learning).

## 🛠️ Tech Stack
* **Language:** Python
* **Database:** PostgreSQL
* **Libraries:** Pandas, SQLAlchemy, Scikit-Learn
* **Machine Learning:** Random Forest Classifier

## 🚀 Key Features & Workflow
1. **ETL Process:** 
   * Loads raw data from `WA_Fn-UseC_-Telco-Customer-Churn.csv`[cite: 1].
   * Splits and inserts data into a PostgreSQL database creating three normalized tables: `customer_demographics`, `customer_services`, and `customer_billing`[cite: 1, 3].
2. **Data Processing:** 
   * Retrieves data using SQL `JOIN` operations across the three tables[cite: 2].
   * Handles hidden missing values (blank spaces) in `total_charges` by converting them to `0`[cite: 2].
3. **Machine Learning Model:** 
   * Encodes categorical data and splits it into 80-20 train-test sets[cite: 2].
   * Trains a `RandomForestClassifier` (100 estimators) to predict if a customer will churn[cite: 2].
4. **Business Insights:** 
   * Extracts feature importances to identify the top 5 reasons driving customer churn[cite: 2].

## 💻 How to Run
1. Create a PostgreSQL database named `telco_db`.
2. Run `schema.sql` to create the tables.
3. Update the PostgreSQL password in the Python scripts.
4. Run `data_loader.py` to populate the database.
5. Run `ml_model.py` to train the model and view accuracy.
