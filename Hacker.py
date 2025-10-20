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
        self.__rig = rig if rig else Rig(owner=self.__name)
        print(f"{self.__name}, your rig is activated and ready for use.")

    def upgrade_rig(self):
        if not self.__rig:
            print(f"{self.__name} has no rig to upgrade.")
            return
        self.__rig.upgrade(self.__inventory)

    def encrypt_asset(self, asset: Asset):
        chip = next((asset for asset in self.__inventory if asset.name == "SecurityChip"), None)
        if not chip:
            print("There are no SecurityChips in inventory for encryption.")
            return
        if asset.encrypted:
            print(f"{asset.name} has already been encrypted.")
            return

        self.__inventory.remove(chip)
        asset.encrypt()
        print(f"{asset.name} encrypted.")

    def decrypt_asset(self, asset: Asset):
        chip = next((asset for asset in self.__inventory if asset.name == "SecurityChip"), None)
        if not chip:
            print("There are no SecurityChips in inventory for decryption.")
            return
        if not asset.encrypted:
            print(f"{asset.name} is not encrypted.")
            return

        self.__inventory.remove(chip)
        asset.decrypt()
        print(f"{asset.name} decrypted.")

    def __str__(self):
        """Return a string representation of the Hacker."""
        rig_status = self.__rig if self.__rig else "No Rig"
        return f"Hacker: {self.__name}\nInventory: {self.__inventory}\nRig: {rig_status}"

    def extract_assets(self, target_rig: Rig):
        drive = next((asset for asset in self.__inventory if asset.name == "RemovableDrive"), None)
        if not drive:
            print("There are no RemovableDrives, unable to complete extraction.")
            return

        self.__inventory.remove(drive)
        unsecured_assets = [asset for asset in target_rig.storage if not asset.encrypted]
        for asset in unsecured_assets:
            self.__inventory.append(asset)
            target_rig.storage.remove(asset)

    def launch_data_spike(self, target_rig: Rig):
        """Attack another rig using DataSpike from hackers own rig's storage."""
        if not self.__rig:
            print("No rig available to launch attack.")
            return
        if self.__trace_level >= self.__trace_limit:
            print(f"{self.__name} is exposed and cannot attack until trace level is reduced!")
            return

        spike = next((asset for asset in self.__rig.storage if asset.name == "DataSpike"), None)
        if not spike:
            print("There are no DataSpikes available in storage to launch attack.")
            return

        self.__rig.storage.remove(spike)
        target_rig.take_hit()
        if target_rig.is_broken():
            self.extract_assets(target_rig)
        self.__trace_level += 1

        print(f"{self.__name} extracted {len(unsecured_assets)} unencrypted assets from {target_rig.name}.")
