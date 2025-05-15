import numpy as np

# Function to calculate performance metrics
def calculate_rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_pred - y_true) ** 2))

# Function to log messages for debugging
def log_message(message):
    # You can expand this function as necessary, e.g., logging to a file
    print(message)
