"""
Module for uploading files from local to cloud
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

Once the first time settings are added you can create the instance
of the FileTransfer class and initiate the transfer

Following is an example:

from upload_to_storage import FileTransfer

# provide your full path to the directory where files are present
root = '/my/path/to/root/directory/'
# create the object
file_transfer = FileTransfer(root)
# verify if files are correctly categorised
print(file_transfer.files)
# Initiate the transfer to S3
file_transfer.upload_files_to_cloud()
"""
from upload_to_storage.main import FileTransfer

__all__ = ['FileTransfer']
