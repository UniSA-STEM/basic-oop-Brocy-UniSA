"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Corey Brooke
ID: 110480857
Username: Brocy076
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import *
from Rig import Rig


class Hacker:
    """
    The Hacker class starts with 3 parameters:
    name: Is a string that will represent the instance of the Hacker class.
    inventory: WIP
    rig: WIP
    """

    def __init__(self, name: str):
        """Initialize the hacker with a name, one CryptoToken, and no rig."""
        self.__name = name
        self.__trace_level = 0
        self.__trace_limit = 5
        self.__rig = None
        self.__inventory = [CryptoToken()]

    def acquire_rig(self, rig: Rig | None = None):
        """Acquire a rig using one CryptoToken.

        Searches the inventory for the first CryptoToken. If found, it is removed
        and a new rig is acquired (or the provided one is activated)."""
    # Finds the first CryptoToken in the inventory list or returns None
        token = next((asset for asset in self.__inventory if asset.name == "CryptoToken"), None)
        if not token:
            print(f"{self.__name} doesn’t have enough CryptoTokens to buy a rig.")
            return

        # Removes the token from the list and creates the Rig
        self.__inventory.remove(token)
        self.__rig = rig if rig else Rig()
        print(f"{self.__name}, your rig is activated and ready for use.")

    def get_trace_level(self):
        return self.__trace_level

    def increase_trace(self, amount: int):
        self.__trace_level += amount
        if self.__trace_level > self.__trace_limit:
            self.__detected = True
            print(f"{self.__name} has been exposed!")

    def launch_data_spike(self, target_rig: Rig):
        """Uses data spike item to do damage to target rig"""
        pass

    def encrypt_assets(self):
        """uses Security Chip item to encrypt assets.

        i think ill just make this a function in asset class"""
        pass

    def decrypt_assets(self):
        """uses Security Chip item to decrypt assets."""
        pass

    def upgrade_rig(self, rig: Rig):
        """uses hardware patch to upgrade rig, upgrade improves storage size and reduces damage taken in battles

        ill use the rig class for this"""
        pass

    def get_inventory(self):
        """I will need to work out the best way to do all the inventory functions"""
        return self.__inventory

    def remove_asset(self, asset):
        if asset in self.__inventory:
            self.__inventory.remove(asset)

    def transfer_asset(self, asset, destination):
        """Transfer an asset from this hacker to another rig or hacker."""
        if asset in self.__inventory:
            self.remove_asset(asset)
            destination.add_asset(asset)
            print(f"{asset} transferred from {self.__name} to {destination}.")
        else:
            print(f"{asset} not found in {self.__name}'s inventory.")

    def __str__(self):
        """Return a string representation of the Hacker."""
        rig_status = self.__rig if self.__rig else "No Rig"
        return f"Hacker: {self.__name}\nInventory: {self.__inventory}\nRig: {rig_status}"
