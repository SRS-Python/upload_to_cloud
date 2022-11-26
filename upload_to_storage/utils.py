"""
This module contains code for all the utilities
The Environments class loads the environment variables
It also uses the dotenv package to identify and load -
all the settings defined in .env file

You can also import the ENV global variable
(an object instance of Environments class)
"""
import os
from dotenv import load_dotenv, find_dotenv


class Environments:
    """
    Class for Environments variable
    Loads all the environment variables, including
    settings defined in .env file
    Example:
        env = Environments()
    """
    env_dict = {}

    def __init__(self):
        """
        Initialization method that loads the .env file
        it also populates the env_dict to store and
        retrieve environment keys.
        """
        load_dotenv(find_dotenv())
        self.env_dict = dict(os.environ)

    def __getattr__(self, item) -> str | None:
        """
        The get attribute method to return value for the key
        Method identifies the key from the env_dict dictionary
        If key not found then returns none
        :param item: key to find in the Environment variable
        :return: value if found, else None
        """
        return self.env_dict.get(item, None)

    def add_key(self, key: str, value: str) -> None:
        """
        The function sets the attribute (stores to env_dict)
        :param key: key to add to environment variable
        :param value: value to add to environment variable
        :return: None
        """
        self.env_dict[key] = value

    def all(self):
        """
        Returns all the environment variable as dict object
        :return: dictionary
        """
        return self.env_dict


# Global variable ENV, which can be used in any program
ENV = Environments()
