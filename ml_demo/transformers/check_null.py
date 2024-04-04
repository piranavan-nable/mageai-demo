if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def check_null(data, *args, **kwargs):

    null_values = data.isnull().sum()
    
    if null_values.sum() == 0:
        return data

    print("ERROR ::::::::: NULL VALUES FOUND")

