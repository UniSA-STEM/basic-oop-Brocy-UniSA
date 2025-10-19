"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Corey Brooke
ID: 110480857
Username: Brocy076
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description
        self.__encrypted = False

    @property
    def name(self):
        return self.__name

    @property
    def encrypted(self):
        return self.__encrypted

    def encrypt(self):
        self.__encrypted = True

    def decrypt(self):
        self.__encrypted = False

    def __str__(self):
        if self.__encrypted:
            return f"{self.__name}: {self.__description} [Encrypted]"
        return f"{self.__name}: {self.__description}"
