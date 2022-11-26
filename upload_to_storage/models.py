"""
This module has definition of all models
It uses dataclass to add basic functionality pre-implemented
"""
from dataclasses import dataclass


@dataclass
class File:
    """
    File dataclass to store the file name,
    file name with path and cloud storage path
    Example:
        file = File(name='file_name',
                    with_path='full_path',
                    path_to='path_on_cloud')
    """
    name: str
    with_path: str
    path_to: str
