
import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform( data, data_2, data_3, data_4, *args, **kwargs):
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
    df1 = pd.DataFrame(data)
    df2 = pd.DataFrame(data_2)
    df3 = pd.DataFrame(data_3)
    df4 = pd.DataFrame(data_4)

    # Specify your transformation logic here
    df = pd.merge(df1, df2, on='ChannelKey', how='left')
    df = pd.merge(df, df3, on='ProductKey', how='left')
    df = pd.merge(df, df4, on='ProductSubCategoryKey', how='left')





    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
