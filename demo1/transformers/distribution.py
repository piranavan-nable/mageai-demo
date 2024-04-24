import matplotlib.pyplot as plt
import pandas as pd

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
    # Specify your transformation logic here
    # Group by 'order_date' and calculate sum of sales for each day
    daily_sales = df.groupby('order_date')['sales'].sum()
    channel_sales = df.groupby('channel_name')['sales'].sum()
    brand_sales = df.groupby('brand_name')['sales'].sum()
    category_sales = df.groupby('product_category')['sales'].sum()

# Plot line plot for time series data
    plt.figure(figsize=(12, 4))
    plt.plot(daily_sales.index, daily_sales.values)
    plt.xlabel('Order Date')
    plt.ylabel('Sales')
    plt.title('Sales Over Time')
    plt.show()

    plt.figure(figsize=(12, 4))
    plt.plot(channel_sales.index, channel_sales.values)
    plt.xlabel('Channel Name')
    plt.ylabel('Sales')
    plt.title('Sales Over Channel')
    plt.show()

    plt.figure(figsize=(12, 4))
    plt.plot(brand_sales.index, brand_sales.values)
    plt.xlabel('Brand Name')
    plt.ylabel('Sales')
    plt.title('Sales Over Brand')
    plt.xticks(rotation=90)
    plt.show()

    plt.figure(figsize=(12, 4))
    plt.plot(category_sales.index, category_sales.values)
    plt.xlabel('Category Name')
    plt.ylabel('Sales')
    plt.title('Sales Over Category')
    plt.show()

    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
