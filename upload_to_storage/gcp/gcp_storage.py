"""
----------------------------------------------------------------------------
This module is responsible for transferring files to Google storage
Google authentication require credentials JSON file.
    i. Place the JSON file in a secure directory
    ii. Add the path along with JSON file name into the .env file
please make sure to add the following keys and values
to the .env file
GCP_CREDENTIAL_FILE=/path/to/credentials/credentials.json
GCP_BUCKET_NAME=your_bucket_name
if the credentials fail, the program will fail to execute
if GCP_BUCKET_NAME is not found, the program will raise exception
Make sure that the user account or service account that you are using
has the required permissions. For this, you must have "storage.buckets.list"
-----------------------------------------------------------------------------
"""
# Imports the Google Cloud client library
from google.cloud import storage
from upload_to_storage.utils import ENV
from upload_to_storage.models import File

GCP_CREDENTIAL_FILE = ENV.GCP_CREDENTIAL_FILE
if GCP_CREDENTIAL_FILE is None:
    raise EnvironmentError('Unable to find GCP_CREDENTIAL_FILE for google storage.')

# validate the bucket name
GCP_BUCKET_NAME = ENV.GCP_BUCKET_NAME
if GCP_BUCKET_NAME is None:
    raise EnvironmentError('You must define GCP_BUCKET_NAME '
                           'in environment variable!')

# Instantiates a client
storage_client = storage.Client.from_service_account_json(GCP_CREDENTIAL_FILE)
# storage_client = storage.Client()

bucket_list = {bucket.name for bucket in storage_client.list_buckets()}
# raise KeyError if bucket name doesn't exist
if GCP_BUCKET_NAME not in bucket_list:
    raise KeyError(f'Unable to find {GCP_BUCKET_NAME} bucket in google storage.')

bucket = storage_client.get_bucket(GCP_BUCKET_NAME)


def upload_to_gcp_storage(file_list: list[File]) -> bool:
    """
    This function uploads the files to GCP storage.
    The parameter is list of File object.
    Function returns the status True at the end.
    Function will raise ValueError,
    if any element is not of File type.
    :type file_list: list[File]
    :param file_list: list of 'File' object
    :raises ValueError if element is not of File class
    :return: status True
    """
    for file in file_list:
        if not isinstance(file, File):
            raise ValueError(f'The object {file}, '
                             f'specified is not a File model!')
        with open(file.with_path, 'rb') as file_obj:
            blob = bucket.blob(file.path_to+file.name)
            blob.upload_from_file(file_obj)
    return True
