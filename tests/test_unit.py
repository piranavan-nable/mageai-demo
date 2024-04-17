import unittest

class TestCI(unittest.TestCase):
    def test_echo(self):
        # Simulate the echo command
        output = "Hello, world!"
        
        # Assert that the output is as expected
        self.assertEqual(output, "Hello, worl!")

if __name__ == '__main__':
    unittest.main()
