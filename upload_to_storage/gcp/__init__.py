"""
This is the main module for GCP programs
The module is dependent on google-cloud-storage
Currently this module supports file upload to google-cloud-storage
"""
import pkg_resources

REQUIRED_PACKAGE = 'google-cloud-storage'
installed = {pkg.key for pkg in set(pkg_resources.working_set)}

if REQUIRED_PACKAGE not in installed:
    MESSAGE = """
    google-cloud-storage is mandatory to upload files to GCP storage
    you can install google-cloud-storage from PyPI with:
    $ pip install google-cloud-storage
    """
    raise ModuleNotFoundError(MESSAGE)
