from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Execute Transformer Action: ActionType.SUM

    Docs: https://docs.mage.ai/guides/transformer-blocks#aggregation-actions
    """
    action = build_transformer_action(
        df,
        action_type=ActionType.SUM,
        action_code='pizza_category != null',  # Enter filtering condition on rows before aggregation
        arguments=["total_price"],  # Enter the columns to compute aggregate over
        axis=Axis.COLUMN,
        options={'groupby_columns': ["pizza_category"]},  # Enter columns to group by
        outputs=[
            # The number of outputs below must match the number of arguments
            {'uuid': 'sum_total_per_category', 'column_type': 'number_with_decimals'},
        ],
    )

    return BaseAction(action).execute(df)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
