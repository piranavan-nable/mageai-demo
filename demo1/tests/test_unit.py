import unittest
import pandas as pd
import os,sys

from demo1.data_loaders.load_data_missing_hdl import load_data_from_file
from demo1.custom.null_check import transform_custom


class test_data_loading_for_prediction(unittest.TestCase):
    def test_handle_missing_values_data_loading(self) :
            

            expected =  pd.read_csv('./data/ML/sales_data_test_ML.csv')
            result = load_data_from_file()
           
            # Compare the lengths of the expected and actual DataFrames
            self.assertEqual(len(expected), len(result), "Length did not match")

            # Compare the column names of the expected and actual DataFrames
            self.assertListEqual(list(expected.columns), list(result.columns),"Column names did not match")
    
    def null_check(self):
        # Create a mock DataFrame for testing
        expected = pd.read_csv('./data/ML/sales_data_test_ML.csv')
        
        # Call the function
        result = transform_custom()
        
        # Assert that the function doesn't return None
        self.assertIsNotNone(result)
        
        # Assert that the result is a DataFrame
        self.assertIsInstance(result, pd.DataFrame)
        
        # Compare null values between original and transformed DataFrames
        original_null_count = expected.isnull().sum().sum()
        transformed_null_count = result.isnull().sum().sum()
        self.assertEqual(original_null_count, transformed_null_count,
                         "Null value counts between original and transformed DataFrames do not match")


if __name__ == '__main__':
    unittest.main()

