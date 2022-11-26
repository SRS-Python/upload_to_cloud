"""This module requires AWS or GCP connection"""
import os.path
import unittest
import pkg_resources
from upload_to_storage import FileTransfer
from upload_to_storage.utils import ENV


class MainTestCase(unittest.TestCase):
    """
    Test class for main module
    """

    def setUp(self):
        """
        Setup class that runs at the beginning
        :return:
        """
        self.gcp_available = 'google-cloud-storage' \
                             in {pkg.key for pkg in pkg_resources.working_set}
        self.root = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'support')

    def test_gcp_negative_bucket_name_missing(self):
        """
        test main with GCP configuration
        :return:
        """
        if not self.gcp_available:
            return
        __temp = ENV.env_dict.copy()
        ENV.env_dict.pop('GCP_BUCKET_NAME', None)
        ENV.env_dict['MEDIA_CLOUD'] = 'GCP'
        ENV.env_dict['IMAGE_CLOUD'] = 'GCP'
        ENV.env_dict['DOCUMENT_CLOUD'] = 'GCP'
        file_transfer = FileTransfer(self.root)
        self.assertRaises(EnvironmentError, file_transfer.upload_files_to_cloud)
        ENV.env_dict = __temp

    def test_gcp_negative_bucket_name_invalid(self):
        """
        test main with GCP configuration
        :return:
        """
        if not self.gcp_available:
            return
        __temp = ENV.env_dict.copy()
        ENV.env_dict['GCP_BUCKET_NAME'] = 'non-existing-bucket'
        ENV.env_dict['MEDIA_CLOUD'] = 'GCP'
        ENV.env_dict['IMAGE_CLOUD'] = 'GCP'
        ENV.env_dict['DOCUMENT_CLOUD'] = 'GCP'
        file_transfer = FileTransfer(self.root)
        self.assertRaises(KeyError, file_transfer.upload_files_to_cloud)
        ENV.env_dict = __temp

    def test_gcp_credentials_missing(self):
        """
        Test the scenario for missing credentials
        :return:
        """
        if not self.gcp_available:
            return
        __temp = ENV.env_dict.copy()
        ENV.env_dict['MEDIA_CLOUD'] = 'GCP'
        ENV.env_dict['IMAGE_CLOUD'] = 'GCP'
        ENV.env_dict['DOCUMENT_CLOUD'] = 'GCP'
        ENV.env_dict.pop('GCP_CREDENTIAL_FILE', None)
        file_transfer = FileTransfer(self.root)
        self.assertRaises(EnvironmentError, file_transfer.upload_files_to_cloud)
        ENV.env_dict = __temp

    def test_gcp_credentials_missing_file(self):
        """
        Test the scenario for missing credentials
        :return:
        """
        if not self.gcp_available:
            return
        __temp = ENV.env_dict.copy()
        ENV.env_dict['MEDIA_CLOUD'] = 'GCP'
        ENV.env_dict['IMAGE_CLOUD'] = 'GCP'
        ENV.env_dict['DOCUMENT_CLOUD'] = 'GCP'
        ENV.env_dict['GCP_CREDENTIAL_FILE'] = '/invalid/gcp/credentials.json'
        file_transfer = FileTransfer(self.root)
        self.assertRaises(FileNotFoundError, file_transfer.upload_files_to_cloud)
        ENV.env_dict = __temp

    def test_gcp_credentials_invalid(self):
        """
        Test the scenario for missing credentials
        :return:
        """
        if not self.gcp_available:
            return
        __temp = ENV.env_dict.copy()
        ENV.env_dict['MEDIA_CLOUD'] = 'GCP'
        ENV.env_dict['IMAGE_CLOUD'] = 'GCP'
        ENV.env_dict['DOCUMENT_CLOUD'] = 'GCP'
        ENV.env_dict['GCP_CREDENTIAL_FILE'] = os.path.join(self.root, 'credentials.json')
        file_transfer = FileTransfer(self.root)
        self.assertRaises(Exception, file_transfer.upload_files_to_cloud)
        ENV.env_dict = __temp

    def test_gcp_upload_positive(self):
        """
        test main with aws s3 configuration
        :return:
        """
        if not self.gcp_available:
            return
        __temp = ENV.env_dict.copy()
        ENV.env_dict['MEDIA_CLOUD'] = 'GCP'
        ENV.env_dict['IMAGE_CLOUD'] = 'GCP'
        ENV.env_dict['DOCUMENT_CLOUD'] = 'GCP'
        file_transfer = FileTransfer(self.root)
        self.assertTrue(file_transfer.upload_files_to_cloud())
        ENV.env_dict = __temp


if __name__ == '__main__':
    unittest.main()
