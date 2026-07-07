import pandas as pd
from sqlalchemy import create_engine
import urllib.parse # Ye library password ke special characters ko fix karegi

# 1. CSV File ko load karna
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# 2. PostgreSQL se connection banana (Bridge)
# Yahan apna asli PostgreSQL password daalein
my_password = '124578'

# Ye line password ko safe format me convert kar degi
safe_password = urllib.parse.quote_plus(my_password)

# Ab safe_password ka use karke engine banayenge
engine = create_engine(f'postgresql://postgres:{safe_password}@localhost:5432/telco_db')

# ... Baaki ka code same rahega (Table 1, Table 2, Table 3 wala) ...

# 3. Data ko 3 hisso me todna aur columns ke naam theek karna

# Table 1: Demographics
df_demo = df[['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents']].copy()
df_demo.columns = ['customer_id', 'gender', 'senior_citizen', 'partner', 'dependents']
df_demo.to_sql('customer_demographics', con=engine, if_exists='append', index=False)

# Table 2: Services
df_services = df[['customerID', 'PhoneService', 'MultipleLines', 'InternetService', 
                  'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 
                  'StreamingTV', 'StreamingMovies']].copy()
df_services.columns = ['customer_id', 'phone_service', 'multiple_lines', 'internet_service', 
                       'online_security', 'online_backup', 'device_protection', 'tech_support', 
                       'streaming_tv', 'streaming_movies']
df_services.to_sql('customer_services', con=engine, if_exists='append', index=False)

# Table 3: Billing
df_billing = df[['customerID', 'Contract', 'PaperlessBilling', 'PaymentMethod', 
                 'MonthlyCharges', 'TotalCharges', 'Churn']].copy()
df_billing.columns = ['customer_id', 'contract', 'paperless_billing', 'payment_method', 
                      'monthly_charges', 'total_charges', 'churn']
df_billing.to_sql('customer_billing', con=engine, if_exists='append', index=False)

print("Badhai ho! Saara data successfully PostgreSQL me load ho gaya hai.")