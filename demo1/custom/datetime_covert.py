import pandas as pd  # Import pandas for data manipulation
from dateutil import parser
import numpy as np


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

    df['order_date'] = pd.to_datetime(df['order_date'],format='%m/%d/%Y', errors='coerce')

    print("Data types:")
    print(df.dtypes)

    return df





@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
