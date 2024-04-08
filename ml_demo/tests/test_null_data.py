import unittest
import pandas as pd
import sys
sys.path.append('./home/src/ml_demo/custom/')   

from prediction import check_null

class TestCheckNullFunction(unittest.TestCase):

    def test_empty_dataframe(self):
        df = pd.DataFrame()
        self.assertEqual(check_null(df), df)

    def test_dataframe_no_null_values(self):
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['a', 'b', 'c']
        })
        self.assertEqual(check_null(df), df)

    def test_dataframe_with_null_values(self):
        df = pd.DataFrame({
            'A': [1, None, 3],
            'B': ['a', 'b', None]
        })
        self.assertIsNone(check_null(df))

    def test_dataframe_mixed_data_types(self):
        df = pd.DataFrame({
            'A': [1, 2.5, 'hello'],
            'B': [True, False, None]
        })
        self.assertIsNone(check_null(df))

    def test_dataframe_missing_columns(self):
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['a', 'b', 'c']
        })
        df_missing_columns = df[['A']]  # DataFrame with missing column 'B'
        self.assertEqual(check_null(df_missing_columns), df_missing_columns)

if __name__ == '__main__':
    unittest.main()
