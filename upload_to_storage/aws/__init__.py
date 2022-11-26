"""
This is the main module for AWS programs
The module is dependent on boto3 SDK from AWS
Currently this module supports file upload to AWS s3
"""
import pkg_resources

REQUIRED_PACKAGE = 'boto3'
installed = {pkg.key for pkg in set(pkg_resources.working_set)}
if REQUIRED_PACKAGE not in installed:
    MESSAGE = """
    boto3 package is required for uploading files to AWS S3
    you can install boto3 from PyPI with:
    $ python3 -m pip install boto3
    or install from source with:
    $ git clone https://github.com/boto/boto3.git
    $ cd boto3
    $ python -m pip install -r requirements.txt
    $ python -m pip install -e ."""
    raise ModuleNotFoundError(MESSAGE)
