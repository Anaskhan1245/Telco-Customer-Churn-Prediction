import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

# 1. Connection (Wahi purana Bridge)
my_password = 'YOUR_PASSWORD' # Yahan par apna sql ka password daalein
safe_password = urllib.parse.quote_plus(my_password)
engine = create_engine(f'postgresql://postgres:{safe_password}@localhost:5432/telco_db')

# 2. Asli Data Scientist wali SQL Query (JOIN)
# Hum teeno tables ko 'customer_id' ke base par jod rahe hain
sql_query = """
SELECT 
    d.customer_id, d.gender, d.senior_citizen, d.partner, d.dependents,
    s.phone_service, s.internet_service, s.online_security, s.tech_support,
    b.contract, b.payment_method, b.monthly_charges, b.total_charges, b.churn
FROM customer_demographics d
JOIN customer_services s ON d.customer_id = s.customer_id
JOIN customer_billing b ON d.customer_id = b.customer_id;
"""

# 3. SQL se direct Pandas me data lana
df = pd.read_sql(sql_query, engine)

# 4. Check karte hain ki data kaisa dikh raha hai
print("Data successfully SQL se Python me aa gaya hai!")
print("-" * 50)
print(df.head()) # Top 5 rows
print("-" * 50)
print(f"Total Rows aur Columns: {df.shape}")


# STEP 5: Data Cleaning (Hidden Error Fix)
print("\n--- Cleaning Data ---")

# 1. Blank spaces ko 'NaN' (Not a Number) me convert karna aur column ko numeric banana
df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')

# 2. Check karna ki kitni rows me error (NaN) aaya
missing_values = df['total_charges'].isnull().sum()
print(f"Hidden blanks found and converted to NaN: {missing_values}")

# 3. Un missing values ko 0 se fill kar dena (Kyunki naye customer ka total bill 0 hoga)
df['total_charges'] = df['total_charges'].fillna(0)

print("Badhai ho! Data Machine Learning ke liye ekdum clean ho gaya hai.")



from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("\n--- Training Machine Learning Model ---")

# NAYA STEP: Sabse pehle 'customer_id' ko original DataFrame se nikal dein
df = df.drop('customer_id', axis=1)

# 1. Encoding (Text ko Numbers 0 aur 1 mein badalna)
df_numeric = pd.get_dummies(df, drop_first=True)

# 2. X aur Y define karna
# Y wo hai jo predict karna hai (Churn), X baaki saari details hain
Y = df_numeric['churn_Yes'] 

# Ab humein 'customer_id' drop karne ki zaroorat nahi hai kyunki wo pehle hi hat chuka hai
X = df_numeric.drop('churn_Yes', axis=1) 

# 3. Train aur Test Split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 4. Model Banana aur Train Karna
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, Y_train) 

# 5. Prediction aur Testing
predictions = model.predict(X_test)
accuracy = accuracy_score(Y_test, predictions)

print(f"Boom! Model Training Complete.")
print(f"Model ki Accuracy: {accuracy * 100:.2f}%")




# --- Task 9: Feature Importance (Kyun bhag rahe hain customers?) ---
print("\n--- Top Reasons for Customer Churn ---")

# Model se importance nikalna
importances = model.feature_importances_
features = X.columns

# Ise ek DataFrame (table) me sajana
importance_df = pd.DataFrame({'Feature': features, 'Importance': importances})

# Sabse zyada importance wale ko upar rakhna
importance_df = importance_df.sort_values(by='Importance', ascending=False)

# Top 5 reasons print karna
print(importance_df.head(5))