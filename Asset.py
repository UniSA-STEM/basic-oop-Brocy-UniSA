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


class CryptoToken(Asset):
    def __init__(self):
        super().__init__("CryptoToken", "Used to acquire or repair rigs.")


class DataSpike(Asset):
    def __init__(self):
        super().__init__("DataSpike", "Used in data battles to damage rigs.")


class RemovableDrive(Asset):
    def __init__(self):
        super().__init__("RemovableDrive", "Used to extract unsecured assets from broken rigs.")


class SecurityChip(Asset):
    def __init__(self):
        super().__init__("SecurityChip", "Used to encrypt or decrypt assets.")


class HardwarePatch(Asset):
    def __init__(self):
        super().__init__("HardwarePatch", "Used to upgrade rigs for better performance.")
