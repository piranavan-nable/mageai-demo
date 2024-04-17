if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def check_data(data, *args, **kwargs):
  
    # Specify your transformation logic here
    c_shape = data.shape
    print(c_shape)
    print()

    c_info = data.info()
    print(c_info)
    print()


    c_des = data.describe()
    print(c_des)
    print()

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
