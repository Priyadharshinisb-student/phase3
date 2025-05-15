import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

# Train the model (should be called only once and save the model)
def train_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, 'housing_price_model.pkl')

# Load the model
def load_model():
    return joblib.load('housing_price_model.pkl')

# Predict function
def predict(data):
    model = load_model()
    return model.predict(data)
