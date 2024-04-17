import unittest
import pandas as pd
import os,sys

sys.path.append('../')  
from ml_demo.transformers.check_null import check_null

class TestCheckNullFunction(unittest.TestCase):

    def test_check_null(self):

        # test 01 -> test with empty df
        df = pd.DataFrame()
        expected_result = pd.DataFrame(index=df.index, columns=df.columns, data=False)
        self.assertTrue(check_null(df).equals(expected_result))

        # test 02 -> test with no null values
        # read data without null values
        df_1 =  pd.read_csv('ml_demo/tests/data/data_without_null.csv')
        self.assertTrue(check_null(df_1).equals(df_1))

        #test 03 -> test with null values
        # Create a DataFrame with null values
        df_2 = pd.read_csv('ml_demo/tests/data/data_with_null.csv')
        result = check_null(df_2) 
        # Assert that the function returns None
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
