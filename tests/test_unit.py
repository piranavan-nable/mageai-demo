import unittest
from demo1.data_loaders.load_data_missing_hdl import load_data_from_file


class ExamplePipelineTest(unittest.TestCase):

    def test_handle_missing_values_data_loading(self):
       
        result = load_data_from_file()
        self.assertIsNotNone(result)
  

if __name__ == '__main__':
    unittest.main()
