import pandas as pd
# Specify your transformation logic here
from sklearn.preprocessing import LabelEncoder

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
    

# Define a label encoder for each categorical variable
    brand_encoder = LabelEncoder()
    category_encoder = LabelEncoder()
    channel_encoder = LabelEncoder()

    # Fit and transform each categorical variable
    df['BrandNameEn'] = brand_encoder.fit_transform(df['brand_name'])
    df['CategoryNameEn'] = category_encoder.fit_transform(df['product_category'])
    df['ChannelNameEn'] = channel_encoder.fit_transform(df['channel_name'])

    # Print the mapping of original categories to encoded values
    print("Brand Name Encoding Mapping:")
    print(dict(zip(brand_encoder.classes_, brand_encoder.transform(brand_encoder.classes_))))
    print("\nCategory Name Encoding Mapping:")
    print(dict(zip(category_encoder.classes_, category_encoder.transform(category_encoder.classes_))))
    print("\nChannel Name Encoding Mapping:")
    print(dict(zip(channel_encoder.classes_, channel_encoder.transform(channel_encoder.classes_))))

    # Drop the original categorical columns if needed
    df.drop(['brand_name', 'product_category', 'channel_name'], axis=1, inplace=True)




    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
