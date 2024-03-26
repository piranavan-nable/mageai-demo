import pandas as pd
from datetime import datetime
from dateutil import parser

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(df: pd.DataFrame,*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here


    try:
        # Convert 'order_date' column to datetime with specified format
        df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    except Exception as e:
        # If an error occurs during conversion, handle it gracefully
        print(f"Error occurred during conversion: {e}")


    # Return the modified DataFrame
    return df



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert isinstance(output, pd.DataFrame), 'Output should be a DataFrame'

    # Check if 'order_date' column has been converted to datetime
    assert output['order_date'].dtype == 'datetime64[ns]', "The 'order_date' column should be of type datetime"
