"""Install the module using pip"""
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='upload_to_cloud',
    version='0.0.1',
    packages=['upload_to_storage'],
    long_description=long_description,
    url='https://github.com/SRS-Python/upload_to_cloud',
    license='Not licensed yet',
    author='Subhendu Sahu',
    author_email='subhendurs.tech@gmail.com',
    description='This module helps in uploading local files to AWS S3 or Google Storage',
    python_requires=">=3.10",
    install_requires=[
        'python-dotenv>=0.21.0',
    ],
    extras_require={
        'AWS_S3': ['boto3'],
        'GCP': ['google-cloud-storage'],
        'ALL': ['boto3', 'google-cloud-storage']
    }
)
