import unittest
import pandas as pd
import os,sys

from demo1.data_loaders.load_data_missing_hdl import load_data_from_file
from demo1.custom.null_check import transform_custom
from demo1.custom.covert_to_date import transform_custom
from demo1.transformers.drop_duplicates import execute_transformer_action
from demo1.custom.crete_features import transform_custom


class test_data_loading_for_prediction(unittest.TestCase):

    def test_handle_missing_values_data_loading(self) :
        expected =  pd.read_csv('./data/ML/sales_data_test_ML.csv')
        result = load_data_from_file()
           
        # Compare the lengths of the expected and actual DataFrames
        self.assertEqual(len(expected), len(result), "Length did not match")

        # Compare the column names of the expected and actual DataFrames
        self.assertListEqual(list(expected.columns), list(result.columns),"Column names did not match")
    
    def null_check(self):
        expected = pd.read_csv('./data/ML/sales_data_test_ML.csv')
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

    def dateTime_convertion_check(self):

        result = transform_custom()

        # Assert that the function doesn't return None
        self.assertIsNotNone(result)
        
        # Assert that the 'order_date' column is converted to datetime
        self.assertEqual(result['order_date'].dtype, 'datetime64[ns]')

    def test_execute_transformer_action_drop_duplicates(self):

        expected = pd.read_csv('./data/ML/sales_data_test_ML.csv')
        result = execute_transformer_action(expected)
        
        # Assert that the function doesn't return None
        self.assertIsNotNone(result)
        
        # Assert that the result is a DataFrame
        self.assertIsInstance(result, pd.DataFrame)
        
        # Assert that the shape of the result is as expected (if all rows are unique, shape should remain the same)
        self.assertEqual(result.shape, expected.drop_duplicates().shape)


    def test_feature_creation(self):

        # Load the expected DataFrame from a CSV file or any other source
        expected_df = pd.read_csv('./data/ML/sales_data_test_ML.csv')
        
        # Call the function to transform the DataFrame
        result_df = transform_custom(expected_df)
        
        # Assert that the function doesn't return None
        self.assertIsNotNone(result_df)
        
        # Assert that the result is a DataFrame
        self.assertIsInstance(result_df, pd.DataFrame)
        
        # Assert that the new columns are added to the DataFrame
        self.assertTrue('year' in result_df.columns)
        self.assertTrue('month' in result_df.columns)
        self.assertTrue('quarter' in result_df.columns)
        self.assertTrue('dayofweek' in result_df.columns)
        self.assertTrue('dayofyear' in result_df.columns)
        self.assertTrue('dayofmonth' in result_df.columns)
        self.assertTrue('weekofyear' in result_df.columns)
        
        # Assert that the values in the new columns are correct
        for index, row in expected_df.iterrows():
            # Extract date components from the 'order_date' column of the expected DataFrame
            expected_year = pd.to_datetime(row['order_date']).year
            expected_month = pd.to_datetime(row['order_date']).month
            expected_quarter = pd.to_datetime(row['order_date']).quarter
            expected_dayofweek = pd.to_datetime(row['order_date']).dayofweek
            expected_dayofyear = pd.to_datetime(row['order_date']).dayofyear
            expected_dayofmonth = pd.to_datetime(row['order_date']).day
            # expected_weekofyear = pd.to_datetime(row['order_date']).isocalendar().week
            isocalendar_tuple = pd.to_datetime(row['order_date']).isocalendar()
            expected_weekofyear = isocalendar_tuple[1]
            
            # Assert that the values in the new columns match the expected values
            self.assertEqual(result_df.loc[index, 'year'], expected_year)
            self.assertEqual(result_df.loc[index, 'month'], expected_month)
            self.assertEqual(result_df.loc[index, 'quarter'], expected_quarter)
            self.assertEqual(result_df.loc[index, 'dayofweek'], expected_dayofweek)
            self.assertEqual(result_df.loc[index, 'dayofyear'], expected_dayofyear)
            self.assertEqual(result_df.loc[index, 'dayofmonth'], expected_dayofmonth)
            self.assertEqual(result_df.loc[index, 'weekofyear'], expected_weekofyear)


if __name__ == '__main__':
    unittest.main()

