"""
Main module that provides capability to Transfer
files from provided path to cloud
All file extension must fall into following category:
    image, media, document
Currently AWS S3 and GCP Cloud Storage are supported
You need specify the settings in .env file
(The sample .env is attached on the repository)
Add following settings to your .env file
---------------General Settings---------------------------
For file extensions, must specify following sections:
    IMAGE_EXT, MEDIA_EXT, DOCUMENT_EXT
Example:
IMAGE_EXT=jpg,png,svg,webp
MEDIA_EXT=mp3,mp4,mpeg4,wmv,3gp,webm
DOCUMENT_EXT=doc,docx,csv,pdf
Next must specify the cloud type sections:
    IMAGE_CLOUD, MEDIA_CLOUD, DOCUMENT_CLOUD
Example:
IMAGE_CLOUD=AWS_S3
MEDIA_CLOUD=AWS_S3
DOCUMENT_CLOUD=GCP
----------------------AWS S3-------------------------------
Note: Client is responsible for creating everything on AWS
(access id, access key, s3 bucket etc)
If you are using AWS S3 -
please make sure to add the following keys and values
to the .env file
AWS_S3_ACCESS_KEY_ID=$your_key_id
AWS_S3_SECRET_ACCESS_KEY=$your_secret_key
S3_BUCKET_NAME=$your_bucket_name
"""
# pylint: disable=import-outside-toplevel

import os
import warnings
from pathlib import Path
from upload_to_storage.models import File
from upload_to_storage.utils import ENV


class FileTransfer:
    """
    This class is the File Transfer Manager to cloud storage
    Currently AWS S3 and GCP storage are supported
    Provide the root directory path while creating object
    E.g:
    file_transfer = FileTransfer('/my/path/to/root/directory')
    When object of this class is created:
        - Gather the files from current and subdirectory
        - Create the file object (refer to models.File)
        - Store the file object to files dictionary
    """

    files = {'media': [], 'image': [], 'document': []}

    def __init__(self, root: str):
        """
        Initialization method of class FileTransfer.
        It requires the root directory details
        :param root: parent directory from while files will be uploaded
        """
        self.root = root
        self.__ext_category = self.files.copy()
        self.current_cloud_service = None
        self.__cloud_service = {'media': '', 'image': '', 'document': ''}
        self.__verify_root()
        self.__verify_required_keys()
        self.__gather_file_list(self.root)

    def __verify_required_keys(self):
        """
        Function verifies if required keys are present in -
        environment variables or not
        If present then populates the __ext_category and __cloud_service dicts
        :return:
        """
        env_all = ENV.all()
        __found_one = False
        for category in self.__ext_category:
            if f'{category.upper()}_EXT' in env_all:
                self.__ext_category[category] = \
                    env_all.get(f'{category.upper()}_EXT').replace(' ', '').split(',')
                __found_one = True
            if f'{category.upper()}_CLOUD' in env_all:
                self.__cloud_service[category] = \
                    env_all.get(f'{category.upper()}_CLOUD')
        if not __found_one:
            raise KeyError('Unable to find at least one extension keys '
                           'in environment variables!')

    def __verify_root(self):
        """
        NOTE: Internal use only
        This method verifies if the root provided exists
        If it doesn't then raise OSError
        :raise OSError
        :return:
        """
        if not os.path.exists(self.root):
            raise OSError(f'{self.root} does not exist!')

    def __gather_file_list(self, path: str, parent_dir: str = ''):
        """
        Note: Internal use only, do not access it outside the class
        This function recursively gathers the files from the -
        parent directory, and store them in files dictionary
        :param path: path to find eligible files
        :param parent_dir: current directory (sourced from root)
        :return: Nothing
        """
        if os.path.isdir(path):
            if path != self.root:
                parent_dir += os.path.basename(path) + '/'
            _ = [self.__gather_file_list(os.path.join(path, sub), parent_dir)
                 for sub in os.listdir(path)]
        else:
            file_ext = os.path.splitext(path)[-1].replace('.', '')
            ext_category = self.__get_category(file_ext)
            if ext_category:
                file = File(name=Path(path).name,
                            with_path=path,
                            path_to=parent_dir)
                self.files[ext_category].append(file)

    def __get_category(self, file_ext: str) -> str | None:
        """
        NOTE: For internal use only
        This method returns the category to which a extension belongs to
        :param file_ext: file extension
        :return: category name
        """
        for key, value in self.__ext_category.items():
            if file_ext in value:
                return key
        return None

    def upload_files_to_cloud(self):
        """
        Method transfers the categorised files to cloud storage
        It identifies the cloud provider from the file category
        Please make sure to add the cloud settings to .env file
            1. identify eligible files in a category
            2. Check if the cloud provider is defined or not
        :return: Nothing
        """
        methods = {'AWS_S3': self.__transfer_to_aws_s3,
                   'GCP': self.__transfer_to_gcp}
        # for all file categories
        for key, value in self.files.items():
            # if there are no files found, move to next record
            if not value:
                continue
            # raise exception if file category is present but cloud provider undefined
            if key not in self.__cloud_service or not self.__cloud_service.get(key, None):
                raise KeyError(f'{key.upper()}_CLOUD must be defined in the .env file')
            # get the name of the cloud provider from settings
            self.current_cloud_service = self.__cloud_service.get(key)
            # find the method name from the provider name
            method = methods.get(self.__cloud_service.get(key), self.transfer_nowhere)
            # call the method
            method(value)
        return True

    @staticmethod
    def __transfer_to_aws_s3(files: list[File]):
        """
        NOTE: For internal use only
        Method is used for uploading files to AWS S3
        The AWS S3 package is imported here as -
        there is a dependency with boto3 package
        You need to install boto3 package, if you want to use this service
        :param files: list of File object to transfer to AWS S3
        :return:
        """
        from upload_to_storage.aws.aws_s3 import upload_to_s3
        upload_to_s3(files)

    @staticmethod
    def __transfer_to_gcp(files):
        """
        NOTE: For internal use only
        Method is used for uploading files to GCP storage
        The gcp storage package is imported here as -
        there is a dependency with google-cloud-storage package
        You need to install google-cloud-storage package, if you want to use this service
        :param files: list of File object to transfer to GCP Storage
        :return:
        """
        from upload_to_storage.gcp.gcp_storage import upload_to_gcp_storage
        upload_to_gcp_storage(files)

    def transfer_nowhere(self, *args, **kwargs):
        """
        This is a placeholder function
        if a cloud provider is not found, then this method is called to warn user
        :return: nothing
        """
        if args or kwargs:
            pass
        warnings.warn(f'{self.current_cloud_service} is not a valid cloud option.')
        # raise RuntimeWarning(f'{self.current_cloud_service} is not a valid cloud option.')
