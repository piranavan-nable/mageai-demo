import unittest
import pandas as pd
import os,sys

sys.path.append('../')  
from ml_demo.transformers.check_null import check_null_val
from ml_demo.transformers.drop_null_values import clean_data

class TestTransformationFunction(unittest.TestCase):

    def test_check_null(self):

        # test 01 -> test with empty df
        df = pd.DataFrame()
        expected_result = pd.DataFrame(index=df.index, columns=df.columns, data=False)
        self.assertTrue(check_null_val(df).equals(expected_result))

        # test 02 -> test with no null values
        # read data without null values
        df_1 =  pd.read_csv('ml_demo/tests/data/data_without_null.csv')
        self.assertTrue(check_null_val(df_1).equals(df_1))

        #test 03 -> test with null values
        # Create a DataFrame with null values
        df_2 = pd.read_csv('ml_demo/tests/data/data_with_null.csv')
        result = check_null_val(df_2) 
        # Assert that the function returns None
        self.assertIsNone(result)


    def test_drop_null(self):

        # Test with empty DataFrame
        df_empty = pd.DataFrame()
        expected_result_empty = pd.DataFrame(index=df_empty.index, columns=df_empty.columns, data=False)
        self.assertIsNone(clean_data(expected_result_empty))
        
        # Test with DataFrame containing null values
        df_null = pd.DataFrame({'A': [1, 2, None, 4],
                                'B': [5, None, 7, 8]})
        expected_result = pd.DataFrame({'A': [1.0,4.0],
                                'B': [5.0,8.0]})
        self.assertTrue(clean_data(df_null).equals(expected_result_null))


if __name__ == '__main__':
    unittest.main()
