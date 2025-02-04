import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset
dataset_path = 'liver_disease_dataset.csv'
data = pd.read_csv(dataset_path)

# Convert gender to numeric (Male = 1, Female = 0)
data['gender'] = data['gender'].map({'Male': 1, 'Female': 0})

# Define features and target
X = data[['age', 'gender', 'total_bilirubin', 'direct_bilirubin', 'alkaline_phosphotase', 'sgot', 'albumin', 'protime']]  # Use the correct columns
y = data['cirrhosis_risk']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the model
model_save_path = 'ml_model/random_forest_model.pkl'
joblib.dump(model, model_save_path)
print(f"Model saved at {model_save_path}")
