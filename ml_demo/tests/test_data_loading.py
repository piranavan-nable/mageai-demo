import unittest
import pandas as pd
import os,sys

sys.path.append('../')  
from ml_demo.data_loaders.load_new_dataset import load_test_data_from_file

class TestDataLoading(unittest.TestCase):

    def test_input_data_forPprediction(self) :

        expected_df =  pd.read_csv('./data/new.csv')
        actual_df = load_test_data_from_file()
        # assert len(excepted_df) == len(actual_df)
        # assert list(excepted_df.columns) == ['customer_id', ' products_purchased', ' complains', ' money_spent']

                # Compare the lengths of the expected and actual DataFrames
        self.assertEqual(len(expected_df), len(actual_df),
                         "Length of expected DataFrame does not match the length of actual DataFrame")

        # Compare the column names of the expected and actual DataFrames
        self.assertListEqual(list(expected_df.columns), 
                             list(actual_df.columns),
                             "Column names of expected DataFrame do not match column names of actual DataFrame")
            
if __name__ == '__main__':
    unittest.main()
