"""This module requires AWS or GCP connection"""
import os
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
        self.aws_available = 'boto3' in {pkg.key for pkg in pkg_resources.working_set}
        self.root = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'support')

    def test_aws_s3_negative_bucket_name_missing(self):
        """
        test main with aws s3 configuration
        :return:
        """
        if not self.aws_available:
            return
        __temp = ENV.env_dict.copy()
        ENV.env_dict.pop('S3_BUCKET_NAME', None)
        ENV.env_dict['MEDIA_CLOUD'] = 'AWS_S3'
        ENV.env_dict['IMAGE_CLOUD'] = 'AWS_S3'
        ENV.env_dict['DOCUMENT_CLOUD'] = 'AWS_S3'
        file_transfer = FileTransfer(self.root)
        self.assertRaises(EnvironmentError, file_transfer.upload_files_to_cloud)
        ENV.env_dict = __temp

    def test_aws_s3_negative_bucket_name_invalid(self):
        """
        test main with aws s3 configuration
        :return:
        """
        if not self.aws_available:
            return
        __temp = ENV.env_dict.copy()
        ENV.env_dict['MEDIA_CLOUD'] = 'AWS_S3'
        ENV.env_dict['IMAGE_CLOUD'] = 'AWS_S3'
        ENV.env_dict['DOCUMENT_CLOUD'] = 'AWS_S3'
        ENV.env_dict['S3_BUCKET_NAME'] = 'non-existing-bucket'
        file_transfer = FileTransfer(self.root)
        self.assertRaises(KeyError, file_transfer.upload_files_to_cloud)
        ENV.env_dict = __temp

    def test_aws_s3_credentials_missing(self):
        """
        Test the scenario for missing credentials
        :return:
        """
        if not self.aws_available:
            return
        __temp = ENV.env_dict.copy()
        ENV.env_dict.pop('AWS_S3_ACCESS_KEY_ID', None)
        ENV.env_dict.pop('AWS_S3_SECRET_ACCESS_KEY', None)
        file_transfer = FileTransfer(self.root)
        self.assertRaises(EnvironmentError, file_transfer.upload_files_to_cloud)
        ENV.env_dict = __temp

    def test_aws_s3_credentials_invalid(self):
        """
        Test the scenario for missing credentials
        :return:
        """
        if not self.aws_available:
            return
        from botocore import exceptions
        __temp = ENV.env_dict.copy()
        ENV.env_dict['MEDIA_CLOUD'] = 'AWS_S3'
        ENV.env_dict['IMAGE_CLOUD'] = 'AWS_S3'
        ENV.env_dict['DOCUMENT_CLOUD'] = 'AWS_S3'
        ENV.env_dict['AWS_S3_ACCESS_KEY_ID'] = 'abcd'
        ENV.env_dict['AWS_S3_SECRET_ACCESS_KEY'] = '12345'
        file_transfer = FileTransfer(self.root)
        self.assertRaises(exceptions.ClientError, file_transfer.upload_files_to_cloud)
        ENV.env_dict = __temp

    def test_aws_s3_upload_positive(self):
        """
        test main with aws s3 configuration
        :return:
        """
        if not self.aws_available:
            return
        __temp = ENV.env_dict.copy()
        ENV.env_dict['MEDIA_CLOUD'] = 'AWS_S3'
        ENV.env_dict['IMAGE_CLOUD'] = 'AWS_S3'
        ENV.env_dict['DOCUMENT_CLOUD'] = 'AWS_S3'
        file_transfer = FileTransfer(self.root)
        self.assertTrue(file_transfer.upload_files_to_cloud())
        ENV.env_dict = __temp


if __name__ == '__main__':
    unittest.main()
