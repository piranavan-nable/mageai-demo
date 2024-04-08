
import pandas as pd  # Import pandas for data manipulation
import numpy as np
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
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

    # Extract hour, day of the week, quarter, month, day of the year, day of the month,
    # and week of the year from the 'order_date' column and add as new features.
    # df['hour'] = df['order_date'].dt.hour
    df['year'] = df['order_date'].dt.year
    df['month'] = df['order_date'].dt.month
    df['quarter'] = df['order_date'].dt.quarter
    df['dayofweek'] = df['order_date'].dt.dayofweek
    df['dayofyear'] = df['order_date'].dt.dayofyear
    df['dayofmonth'] = df['order_date'].dt.day
    df['weekofyear'] = df['order_date'].dt.isocalendar().week
    
    # Return the DataFrame with added features.
    return df



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

