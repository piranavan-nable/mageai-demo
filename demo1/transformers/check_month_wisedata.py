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
    # Assuming 'order_date' is in datetime format
    # Filter the DataFrame for January 2014
    jan_2014_data = df[(df['order_date'].dt.year == 2012) & (df['order_date'].dt.month == 1)]

    # Group by 'order_date' (day) and sum the 'sales' for each day
    daily_sales_jan_2014 = jan_2014_data.groupby(jan_2014_data['order_date'].dt.day)['sales'].sum()

#    Display the total sales for each day in January 2014
    print("Total Sales for Each Day in January 2014:")
    print(daily_sales_jan_2014)


    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
