from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import io

def generate_plot_and_metrics():
    matplotlib.use('Agg')
    sns.set()  # Set Seaborn style for the plot

    housing = fetch_california_housing()
    X, y = housing.data, housing.target

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict on test data
    y_pred = model.predict(X_test)

    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    metrics = {'MSE': mse, 'R^2': r2, 'MAE': mae}

    # Generate a plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=X_test[:, 0], y=y_test, color='green', label='Actual', s=50)  # s is the size of the dots
    sns.lineplot(x=X_test[:, 0], y=y_pred, color='orange', label='Predicted', linewidth=2)
    plt.xlabel('Feature')
    plt.ylabel('Target')
    plt.title('Regression Plot')
    plt.legend()

    # Save plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)

    return buf, metrics
