import pandas as pd

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(df: pd.DataFrame, *args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    print("Data types:")
    print(df.dtypes)

    return df
    # Initialize an empty dictionary to store column names and their data types
    # data_types = {}

    # # Iterate through each column in the DataFrame
    # for column in df.columns:
    #     # Get the data type of the column and store it in the dictionary
    #     data_types[column] = str(df[column].dtype)

    # # Return the dictionary containing column names and their data types
    # return data_types


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
