"""
---------------------------------------------------------------
This module is responsible for transferring files to AWS S3
The module is dependent on boto3 SDK from AWS
please make sure to add the following keys and values
to the .env file
AWS_S3_ACCESS_KEY_ID=$your_key_id
AWS_S3_SECRET_ACCESS_KEY=$your_secret_key
S3_BUCKET_NAME=$your_bucket_name
if the credentials fail, the program will fail to execute
if S3_BUCKET_NAME is not found, the program will raise exception
-----------------------------------------------------------------
"""
import boto3
from upload_to_storage.models import File
from upload_to_storage.utils import ENV

AWS_S3_ACCESS_KEY_ID = ENV.AWS_S3_ACCESS_KEY_ID
AWS_S3_SECRET_ACCESS_KEY = ENV.AWS_S3_SECRET_ACCESS_KEY

# validate if AWS key and id are configured
if AWS_S3_ACCESS_KEY_ID is None or AWS_S3_SECRET_ACCESS_KEY is None:
    raise EnvironmentError('You must set AWS_S3_ACCESS_KEY_ID '
                           'and AWS_S3_SECRET_ACCESS_KEY '
                           'in environment variable!!')

# validate the bucket name
S3_BUCKET_NAME = ENV.S3_BUCKET_NAME
if S3_BUCKET_NAME is None:
    raise EnvironmentError('You must define S3_BUCKET_NAME '
                           'in environment variable!')

# create a session with AWS using the key and id

session = boto3.Session(
    aws_access_key_id=AWS_S3_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_S3_SECRET_ACCESS_KEY,
)


# find the S3 bucket
s3 = session.resource('s3')
bucket_list = {bucket.name for bucket in s3.buckets.all()}
# raise KeyError if bucket name doesn't exist
if S3_BUCKET_NAME not in bucket_list:
    raise KeyError(f'Unable to find {S3_BUCKET_NAME} bucket in AWS S3.')

# create the bucket instance of S3
bucket = s3.Bucket(S3_BUCKET_NAME)


def upload_to_s3(file_list: list[File]) -> bool:
    """
    This function uploads the files to AWS S3.
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
        bucket.upload_file(file.with_path, file.path_to+file.name)
    return True
