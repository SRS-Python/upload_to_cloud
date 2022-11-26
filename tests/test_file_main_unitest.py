"""Test the main module functionalities"""
import os
import unittest
from upload_to_storage import FileTransfer
from upload_to_storage.utils import ENV


class MainTestCase(unittest.TestCase):
    """Test class for testing main module"""
    def setUp(self):
        """
        Setup class that runs at the beginning
        :return:
        """
        self.root = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'support')

    def test_main_object_creation_negative(self):
        """
        Negative testing for
        :return:
        """
        root = '/foo/bar/'
        self.assertRaises(OSError, FileTransfer, root)

    def test_main_object_creation_positive(self):
        """
        Negative testing for
        :return:
        """
        file_transfer = FileTransfer(self.root)
        self.assertIsNotNone(file_transfer.files)
        self.assertIsInstance(file_transfer.files, dict)

    def test_main_file_extension_keys_negative(self):
        """
        Test if the file extension keys are present
        raises exception
        :return:
        """
        __temp = ENV.env_dict.copy()
        ENV.env_dict.pop('MEDIA_EXT', None)
        ENV.env_dict.pop('IMAGE_EXT', None)
        ENV.env_dict.pop('DOCUMENT_EXT', None)
        self.assertRaises(KeyError, FileTransfer, self.root)
        ENV.env_dict = __temp

    def test_main_invalid_cloud_provider(self):
        """
        Test the invalid cloud provider case
        :return:
        """
        __temp = ENV.env_dict.copy()
        ENV.env_dict['MEDIA_CLOUD'] = 'MY_CLOUD'
        ENV.env_dict.pop('IMAGE_EXT', None)
        ENV.env_dict.pop('DOCUMENT_EXT', None)
        ENV.env_dict.pop('IMAGE_CLOUD', None)
        ENV.env_dict.pop('DOCUMENT_CLOUD', None)
        file_transfer = FileTransfer(self.root)
        self.assertWarns(UserWarning, file_transfer.upload_files_to_cloud)
        ENV.env_dict = __temp

    def test_main_undefined_cloud_provider(self):
        """
        Test the undefined cloud provider case
        :return:
        """
        __temp = ENV.env_dict.copy()
        ENV.env_dict.pop('IMAGE_EXT', None)
        ENV.env_dict.pop('DOCUMENT_EXT', None)
        ENV.env_dict.pop('MEDIA_CLOUD', None)
        ENV.env_dict.pop('IMAGE_CLOUD', None)
        ENV.env_dict.pop('DOCUMENT_CLOUD', None)
        file_transfer = FileTransfer(self.root)
        self.assertRaises(KeyError, file_transfer.upload_files_to_cloud)
        ENV.env_dict = __temp


if __name__ == '__main__':
    unittest.main()
