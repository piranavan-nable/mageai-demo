if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@transformer
def check_null_val(data, *args, **kwargs):

    null_values = data.isnull().sum()
    
    if null_values.sum() == 0:
        return data

    print("ERROR ::::::::: NULL VALUES FOUND")


@test
def test_output(output, *args) -> None:

    assert output is not None, 'The output is undefined'
    assert isinstance(output, pd.DataFrame)
    assert len(output) == 13
