"""This a test module to test finding files in a directory"""
import unittest
from upload_to_storage.models import File


class FileTestCase(unittest.TestCase):
    """Class for testing File model"""

    def test_file_object_creation(self):
        """
        Test the creation of File object
        :return:
        """
        file = File('a', 'b', 'c')
        self.assertEqual(file.name, 'a')
        self.assertEqual(file.path_to, 'c')
        self.assertEqual(file.with_path, 'b')

    def test_file_object_creation_negative(self):
        """
        Test invalid number of parameters to File class
        :return:
        """
        self.assertRaises(TypeError, File, 'a')


if __name__ == '__main__':
    unittest.main()
