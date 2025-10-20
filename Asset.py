"""
File: Asset.py
Description: This file contains code for basic asset creation, used by the Hacker and Rig files.
Author: Corey Brooke
ID: 110480857
Username: Brocy076
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    """Base class with each instance representing a digital asset.

    Attributes:
        __name (str): The name of the asset.
        __description (str): A brief description of what the asset does.
        __encrypted (bool): Whether the asset is currently encrypted."""

    def __init__(self, name: str, description: str):
        """Sets up the asset."""
        self.__name = name
        self.__description = description
        self.__encrypted = False

    @property
    def name(self):
        """Return the asset's name."""
        return self.__name

    @property
    def encrypted(self):
        """Returns if the asset is encrypted as a Boolean value with True meaning that the asset is encrypted."""
        return self.__encrypted

    def encrypt(self):
        """Encrypt the asset, marking it as protected and non-transferable."""
        self.__encrypted = True

    def decrypt(self):
        """Decrypt the asset, allowing it to be transferred or used again."""
        self.__encrypted = False

    def __str__(self):
        """Returns a string showing the asset's name, description, and an [Encrypted] tag if the asset is protected."""
        if self.__encrypted:
            return f"{self.__name}: {self.__description} [Encrypted]"
        return f"{self.__name}: {self.__description}"

# --------------< Subclasses representing the types of assets that can be made. >--------------

class CryptoToken(Asset):
    """Used to acquire or repair rigs."""
    def __init__(self):
        super().__init__("CryptoToken", "Used to acquire or repair rigs.")


class DataSpike(Asset):
    """Used to damage other rigs."""
    def __init__(self):
        super().__init__("DataSpike", "Used in data battles to damage rigs.")


class RemovableDrive(Asset):
    """Used to extract unencrypted assets."""
    def __init__(self):
        super().__init__("RemovableDrive", "Used to extract unsecured assets from broken rigs.")


class SecurityChip(Asset):
    """Used to encrypt and decrypt assets."""
    def __init__(self):
        super().__init__("SecurityChip", "Used to encrypt or decrypt assets.")


class HardwarePatch(Asset):
    """Used to upgrade a Rigs."""
    def __init__(self):
        super().__init__("HardwarePatch", "Used to upgrade rigs for better performance.")
