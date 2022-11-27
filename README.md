upload_to_cloud
=================
**upload_to_cloud** is a python package that helps in transferring your local files to cloud storage. 
Currently AWS S3 or Google Cloud Storage are supported for file upload.
Please refer the following guide for installation steps.

**Note: The current version requires Python 3.10+**

- [pre-requisites](#pre-requisites)
  - [AWS Requirement](#aws-requirement)
  - [Google Cloud Storage Requirements](#google-cloud-storage-requirements)
- [Getting Started](#getting-started)
- [For Developers](#for-developers)
- [Work in Progress](#work-in-progress)

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

### Google Cloud Storage Requirements
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
- [Google-Cloud-Storage](#google-cloud-storage)
- [All-cloud-providers](#all-cloud-providers)

#### AWS-S3
This step is applicable if you only use AWS S3 to upload your files.

You can install the package from source with following:
```shell
$ git clone https://github.com/SRS-Python/upload_to_cloud.git
$ cd upload_to_cloud
$ python -m pip install -r requirements_aws.txt
$ python -m pip install -e .
```

#### Google-Cloud-Storage
This step is applicable if you only use Google Cloud Storage to upload your files.

You can install the package from source with following:
```shell
$ git clone https://github.com/SRS-Python/upload_to_cloud.git
$ cd upload_to_cloud
$ python -m pip install -r requirements_gcp.txt
$ python -m pip install -e .
```

#### All-cloud-providers
If you want to work on either AWS S3 or Google Cloud Storage, you can follow the below steps:

```shell
$ git clone https://github.com/SRS-Python/upload_to_cloud.git
$ cd upload_to_cloud
$ python -m pip install -r requirements.txt
$ python -m pip install -e .
```

Once the package is installed, you can run the following program:
Note: _you need to import `upload_to_storage` module._
```shell
# Import the FileTransfer class from upload_to_storage
from upload_to_storage import FileTransfer

# Define the path where your file is present
files_root = '/path/to/files/'
# Create the object for FileTransfer by passing the files root
# Note: files root is a required parameter
file_transfer=FileTransfer(files_root)
# Call the upload_files_to_cloud method to transfer the files
file_transfer.upload_files_to_cloud()
```

## For Developers

If you want to run the pytest, please follow the below steps:
- Install the dev requirements on the project root
```shell
# please move to upload_to_cloud directory, then run following
$ python -m pip install -r requirements_dev.txt
```
- Test the module from command line
```shell
# please move to upload_to_cloud directory, then run following
$ pytest ./tests
```
- Note: The above test will run system test as well. 
Please have AWS and/or GCP storage package installed: [All-cloud-providers](#all-cloud-providers)
- You can also test individual modules as well as follows:
```shell
# please move to upload_to_cloud directory, then run following
$ pytest ./tests/test_file_main_unitest.py
```

## Work in Progress
- Current version of code doesn't generate any message to the end users when process completes.
- Enable logging and log level for verbose messages.