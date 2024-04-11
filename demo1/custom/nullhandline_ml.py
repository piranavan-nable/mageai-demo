import pandas as pd
import numpy as np
import joblib
from sklearn.impute import SimpleImputer

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(data, *args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """



    # Load the previously trained XGBoost model
    model = joblib.load('xgboost_model_sales.pkl')

    # Define your features
    FEATURES = ['year', 'month', 'quarter', 'dayofweek', 'dayofyear', 'dayofmonth', 'weekofyear','order_qty','price','CategoryNameEn','BrandNameEn','ChannelNameEn']
    TARGET = 'sales'

    # Check for null values in the 'sales' column
    null_sales_indices = data[data['sales'].isnull()].index

    # Fill null values in 'sales' column using the trained model
    for index in null_sales_indices:
        # Extract features for prediction
        features = data.loc[index, FEATURES].values.reshape(1, -1)
        
        # Predict sales value
        predicted_sales = model.predict(features)

        
        # Fill null value with predicted sales
        data.at[index, 'sales'] = predicted_sales[0]

    # Save the updated dataset
    data.to_csv('./mage_data/demo1/ML/sales_data_null_filled.csv', index=False, float_format='%.2f')  # Save the dataset to a new CSV file

    # Print only the 'order_date' and 'sales' columns for the predicted rows with sales rounded to 2 decimal places
    predicted_rows = data.loc[null_sales_indices, ['order_date', 'sales']].round({'sales': 2})
    print(predicted_rows)

    print(data.isnull().sum())
    print(data.info())


    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
