if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(df, *args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here
    # Extract year, day of the week, quarter, month, day of the year, day of the month,
    # and week of the year from the 'order_date' column 
    df['year'] = df['order_date'].dt.year
    df['month'] = df['order_date'].dt.month
    df['quarter'] = df['order_date'].dt.quarter
    df['dayofweek'] = df['order_date'].dt.dayofweek
    df['dayofyear'] = df['order_date'].dt.dayofyear
    df['dayofmonth'] = df['order_date'].dt.day
    df['weekofyear'] = df['order_date'].dt.isocalendar().week

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
