import mlflow
import mlflow.sklearn

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import io
# used for datasets
import pandas as pd
# used for log transform
import numpy as np

def generate_plot_and_metrics():
    # Use the 'Agg' backend for Matplotlib
    matplotlib.use('Agg')
    sns.set()  # Set Seaborn style for the plot

    # Enable automatic logging to MLflow
    mlflow.set_experiment("Zillow Test")
    mlflow.autolog()

    # Load the Iris dataset
    #X, y = datasets.load_iris(return_X_y=True)
    dataset = pd.read_csv('./data/Housing.csv')
    X = dataset[['area']]
    y = dataset['price']
    ln_X = np.log(X)
    ln_Y = np.log(y)

    # Split the data into training and test sets
    _X_train, _X_test, _y_train, _y_test = train_test_split(ln_X, ln_Y, test_size=0.5, random_state=0)

    # Define the model hyperparameters
    params = {}

    # Train the model
    _lr = LinearRegression(**params)
    _lr.fit(_X_train, _y_train)

    # Predict on the test set
    _y_pred = _lr.predict(_X_test)

    # Start MLflow run
    with mlflow.start_run():
        # Train the model
        _lr = LinearRegression(**params)
        _lr.fit(_X_train, _y_train)

        # Predict on the test set
        _y_pred = _lr.predict(_X_test)

        # Calculate metrics
        mse = mean_squared_error(_y_test, _y_pred)
        r2 = r2_score(_y_test, _y_pred)
        mae = mean_absolute_error(_y_test, _y_pred)
        metrics = {'MSE': mse, 'R^2': r2, 'MAE': mae}

        # Log metrics manually (optional, since autolog will capture them)
        mlflow.log_metric('MSE', mse)
        mlflow.log_metric('R2', r2)
        mlflow.log_metric('MAE', mae)

        # Log model manually (optional, since autolog will capture it)
        mlflow.sklearn.log_model(_lr, "linear-regression-model")

        # Generate a plot
        plt.figure(figsize=(10, 6))
        plt.scatter(np.exp(_X_train), np.exp(_y_train), label='Actual', color='red')
        plt.plot(np.exp(_X_test), np.exp(_y_pred), label='Predicted', color='blue', linewidth=3)
        plt.xlabel('House Features')
        plt.ylabel('Price')
        plt.title('Log-Transformed Linear Regression - House Features vs. Price')
        plt.legend()

        # Save plot to a bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        buf.seek(0)

    return buf, metrics

