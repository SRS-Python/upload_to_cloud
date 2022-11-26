"""Test if the file object used for upload is of type `File`"""
import unittest
import pkg_resources


class FileObjectTestCase(unittest.TestCase):
    """
    Test class for valid object type for file upload
    """
    def setUp(self):
        """
        Setup class that runs at the beginning
        :return:
        """
        self.gcp_available = 'google-cloud-storage' \
                             in {pkg.key for pkg in pkg_resources.working_set}
        self.aws_available = 'boto3' \
                             in {pkg.key for pkg in pkg_resources.working_set}

    def test_gcp_invalid_file_object(self):
        """
        Test if the object type is valid or not
        for the upload_to_gcp_storage function
        :return:
        """
        if not self.gcp_available:
            return
        from upload_to_storage.gcp.gcp_storage import upload_to_gcp_storage
        self.assertRaises(ValueError, upload_to_gcp_storage, [{'name': 'dummy'}])

    def test_aws_invalid_file_object(self):
        """
        Test if the object type is valid or not
        for the upload_to_gcp_storage function
        :return:
        """
        if not self.aws_available:
            return
        from upload_to_storage.aws.aws_s3 import upload_to_s3
        self.assertRaises(ValueError, upload_to_s3, [{'name': 'dummy'}])


if __name__ == '__main__':
    unittest.main()
