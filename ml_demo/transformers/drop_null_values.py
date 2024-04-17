if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def clean_data(data, *args, **kwargs):
    
    if data.empty:  # Check if the DataFrame is empty
        return None
    else:
        data_cleaned = data.dropna()
        return data_cleaned


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
