import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import xgboost as xgb
import pickle



import pandas as pd  # Import pandas for data manipulation
import numpy as np
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    # Specify the date for splitting (e.g., '2014-06-01' as the cutoff date)
    split_date = '2014-06-01'

    # Split the data into training and testing sets
    train = data[data['order_date'] < split_date]
    test = data[data['order_date'] >= split_date]

    # Display the shapes of the training and testing sets
    print("Training set shape:", train.shape)
    print("Testing set shape:", test.shape)

    FEATURES = ['year', 'month', 'quarter', 'dayofweek', 'dayofyear', 'dayofmonth', 'weekofyear','order_qty','price','CategoryNameEn','BrandNameEn','ChannelNameEn']
    TARGET = 'sales'

    # Extract features (X) and target variable (y) for training dataset.
    X_train = train[FEATURES]
    y_train = train[TARGET]

    # Extract features (X) and target variable (y) for testing dataset.
    X_test = test[FEATURES]
    y_test = test[TARGET]

    # Create an XGBoost regressor with specified hyperparameters.
    reg = xgb.XGBRegressor(
        base_score=0.5,
        booster='gbtree',
        n_estimators=10000,
        early_stopping_rounds=50,
        objective='reg:linear',
        max_depth=3,
        learning_rate=0.01
    )

    # Fit the XGBoost regressor to the training data and validate on the test set.
    reg.fit(
    X_train, y_train,
    eval_set=[(X_train, y_train), (X_test, y_test)],
    verbose=100
    )

    

    # Predict the sales on the training and testing datasets
    y_train_pred = reg.predict(X_train)
    y_test_pred = reg.predict(X_test)


    # Calculate evaluation metrics for training set
    mae_train = mean_absolute_error(y_train, y_train_pred)
    mse_train = mean_squared_error(y_train, y_train_pred)
    rmse_train = mse_train ** 0.5
    r2_train = r2_score(y_train, y_train_pred)

    # Print the evaluation metrics
    print("Training Set Metrics:")
    print("MAE:", mae_train)
    print("MSE:", mse_train)
    print("RMSE:", rmse_train)
    print("R-squared:", r2_train)

    test['prediction'] = reg.predict(X_test)
    df = data.merge(test[['prediction']], how='left', left_index=True, right_index=True)

    # Assuming SalesDate is a datetime column, convert it to the index
    df.set_index('order_date', inplace=True)

    # Plot the TotalSales column
    ax = df[['sales']].plot(figsize=(15, 5))

    # Plot the predictions using the 'prediction' column
    df['prediction'].plot(ax=ax, style='.')

    # Add legend and title
    plt.legend(['Truth Data', 'Predictions'])
    ax.set_title('Raw Data and Prediction')

    # Show the plot
    plt.show()

    with open('./data/xgboost_model_sales.pkl', 'wb') as f:
        pickle.dump(reg, f)

    return test

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
