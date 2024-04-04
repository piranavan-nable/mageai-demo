if 'condition' not in globals():
    from mage_ai.data_preparation.decorators import condition


@condition
def evaluate_condition(data, *args, **kwargs) -> bool:
    null_values = data.isnull().sum()

    if null_values > 0:
        return data
