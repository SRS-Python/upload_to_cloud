"""Testing for utils module"""
import unittest
from upload_to_storage.utils import Environments, ENV


class UtilsTestCase(unittest.TestCase):
    """Test class for utils module"""
    def test_environment_positive(self):
        """
        Test the all method
        :return:
        """
        self.maxDiff = None
        my_env = Environments()
        self.assertIsInstance(my_env.all(), dict)
        self.assertIsInstance(ENV.all(), dict)

    def test_environment_key_positive(self):
        """
        Test the value of the key if key present
        :return:
        """
        ENV.add_key('TEST', 'Test')
        self.assertIsNotNone(ENV.TEST)

    def test_environment_key_negative(self):
        """
        Test the value of the key if key not present
        :return:
        """
        self.assertIsNone(ENV.TEST)


if __name__ == '__main__':
    unittest.main()
