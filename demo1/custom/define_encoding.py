import pandas as pd  # Import pandas for data manipulation
import numpy as np
import matplotlib.pyplot as plt

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(df,*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here
    
    # Define the encoding mappings
    brand_encoding_mapping = {'A. Datum': 0, 'Adventure Works': 1, 'Adventure Works ': 2, 'Contoso': 3, 'Fabrikam': 4, 'Fabrikam  ': 5, 'Litware': 6, 'Litware ': 7, 'Northwind Traders': 8, 'Proseware': 9, 'Southridge Video': 10, 'The Phone Company': 11, 'Wide World Importers': 12}
    category_encoding_mapping = {'Audio': 0, 'Cameras and camcorders ': 1, 'Cell phones': 2, 'Computers': 3, 'Music, Movies and Audio Books': 4, 'TV and Video': 5}
    channel_encoding_mapping = {'Mobile Outlet': 0, 'Online': 1, 'Reseller': 2, 'Store': 3}



    # Apply encoding to DataFrame
    df['BrandNameEn'] = df['brand_name'].map(brand_encoding_mapping)
    df['CategoryNameEn'] = df['product_category'].map(category_encoding_mapping)
    df['ChannelNameEn'] = df['channel_name'].map(channel_encoding_mapping)

    # Drop original columns 
    df.drop(columns=['brand_name', 'product_category', 'channel_name'], inplace=True)
    

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
