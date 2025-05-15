import pandas as pd

def preprocess_data(data):
    # Example preprocessing steps
    # Normally, you would handle missing values, encoding, etc.
    
    # For this implementation, let's assume we're normalizing income
    data['Income'] = normalize_income(data['Income'])
    return data

# Example normalization function
def normalize_income(income_series):
    return (income_series - income_series.mean()) / income_series.std()
