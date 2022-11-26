upload_to_storage
=================
**upload_to_storage** helps in transferring your local files to cloud storage. Currently it is supporting upload to AWS S3 or Google Cloud Storage.
Please refer the following guide for installation steps.

- [pre-requisites](#pre-requisites)
  - [AWS Requirement](#aws-requirement)
  - [Google Cloud Storage](#google-cloud-storage)
- [Getting Started](#getting-started)

## pre-requisites
Your project would require a `.env` file. Sample file is attached to the project. refer: `.env_example`

Currently, the library supports images, media and documents to be transferred.
Set the extension keys as shown in the example.
If you don't want to transfer certain type of category, leave them blank or remove the key.
_Note: Don't alter the key names `IMAGE_EXT`, `MEDIA_EXT`, `DOCUMENT_EXT`._
```shell
# Set the file extensions to each category
IMAGE_EXT=jpg,png,svg,webp,jpeg
MEDIA_EXT=mp3,mp4,mpeg4,wmv,3gp,webm
DOCUMENT_EXT=doc,docx,csv,pdf
```
You would also be required to set the cloud provider as well to transfer the file.
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
Please add the following section in the `.env` file.

_Note: Client is responsible for creating the access key and bucket from aws._

[How to order AWS key?](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)
```shell
# Following sections are required for AWS configuration
AWS_S3_ACCESS_KEY_ID=your_key_id
AWS_S3_SECRET_ACCESS_KEY=your_access_key
S3_BUCKET_NAME=your_bucket_name
```

### Google Cloud Storage
Please add the following section in the `.env` file for GCP Storage.
GCP authentication requires credentials.json file. 
Download the JSON to a secure folder and place the path of same into the `.env` under `GCP_CREDENTIAL_FILE` section.

_Note: Client is responsible for getting the credentials.json and bucket from GCP._

[How to create GCP credentials?](https://developers.google.com/workspace/guides/create-credentials)
```shell
# Following sections are required for AWS configuration
GCP_CREDENTIAL_FILE=/path/to/credentials/credentials.json
GCP_BUCKET_NAME=your_bucket_name
```

## Getting Started
