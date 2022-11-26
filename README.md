upload_to_storage
=================
**upload_to_storage** is a python package that helps in transferring your local files to cloud storage. 
Currently AWS S3 or Google Cloud Storage are supported for file upload.
Please refer the following guide for installation steps.

**Note: The current code requires Python 3.10+**

- [pre-requisites](#pre-requisites)
  - [AWS Requirement](#aws-requirement)
  - [Google Cloud Storage](#google-cloud-storage)
- [Getting Started](#getting-started)

## pre-requisites
Your project would require a `.env` file. Sample file is attached to the project. refer: `.env_example`

Currently, the library supports images, media and documents to be transferred.
Set the extension keys as shown in the example below.

If you don't want to transfer certain type of category, leave them blank or remove the key.
_Note: Don't alter the key names `IMAGE_EXT`, `MEDIA_EXT`, `DOCUMENT_EXT`._
```shell
# Set the file extensions to each category
IMAGE_EXT=jpg,png,svg,webp,jpeg
MEDIA_EXT=mp3,mp4,mpeg4,wmv,3gp,webm
DOCUMENT_EXT=doc,docx,csv,pdf
```
You would also be required to set the cloud provider details to transfer the file.
Refer the following example:
```shell
# Set the cloud provider name as mentioned below
IMAGE_CLOUD=AWS_S3
MEDIA_CLOUD=AWS_S3
DOCUMENT_CLOUD=GCP
```
_Note: Don't alter the key names `IMAGE_CLOUD`, `MEDIA_CLOUD`, `DOCUMENT_CLOUD`.
      Only supported values are `AWS_S3` or `GCP`_

### AWS Requirement
If you are using AWS S3, please add the following section to the `.env` file.

_Note: Client is responsible for creating the access key and bucket from aws._

[How to order AWS key?](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)
```shell
# Following sections are required for AWS S3
AWS_S3_ACCESS_KEY_ID=your_key_id
AWS_S3_SECRET_ACCESS_KEY=your_access_key
S3_BUCKET_NAME=your_bucket_name
```

### Google Cloud Storage
If you are using Google Cloud Storage, please add the following section in the `.env` file.
To authenticate with Google cloud, credentials json file is mandatory. 
Download the JSON to a secure location and add the path to the `.env` under `GCP_CREDENTIAL_FILE` section.

_Note: Client is responsible for getting the credentials.json and bucket from GCP._

[How to create GCP credentials?](https://developers.google.com/workspace/guides/create-credentials)
```shell
# Following sections are required for Google Cloud Storage
GCP_CREDENTIAL_FILE=/path/to/credentials/credentials.json
GCP_BUCKET_NAME=your_bucket_name
```

## Getting Started
Assuming that you have a supported version of Python installed, you can first set up your environment with:
```shell
$ python -m venv venv
...
$ . venv/bin/activate
```
Jump to the section as per your cloud configuration:
- [AWS-S3](#aws-s3)
- [Google-Cloud-Storage](#gcp-storage)
- [All-cloud-providers](#all-cloud)

#### AWS-S3
This step is applicable if you only use AWS S3 to upload your files.

You can install the package from source with following:
```shell
$ git clone https://github.com/SRS-Python/upload_to_cloud.git
$ cd boto3
$ python -m pip install -r requirements_aws.txt
$ python -m pip install -e .
```

#### Google-Cloud-Storage
This step is applicable if you only use Google Cloud Storage to upload your files.

You can install the package from source with following:
```shell
$ git clone https://github.com/SRS-Python/upload_to_cloud.git
$ cd boto3
$ python -m pip install -r requirements_gcp.txt
$ python -m pip install -e .
```

#### All-cloud-providers
If you want to work on either AWS S3 or Google Cloud Storage, you can follow the below steps:

```shell
$ git clone https://github.com/SRS-Python/upload_to_cloud.git
$ cd boto3
$ python -m pip install -r requirements.txt
$ python -m pip install -e .
```

Once the package is installed, you can run the following program:
```shell
from upload_to_storage import FileTransfer

# Add the path where your file is present
files_root = '/path/to/files/'
file_transfer=FileTransfer(files_root)
file_transfer.upload_files_to_cloud()
```
