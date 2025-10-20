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

    def store_asset(self, asset_name: str = "", all_items: bool = False):
        if not self.__rig:
            print(f"{self.__name} has no rig to store assets in.")
            return

        if all_items:
            movable_assets = [asset for asset in self.__inventory if not asset.encrypted]
            if not movable_assets:
                print("No movable (unencrypted) assets found in inventory.")
                return

            self.__inventory = [asset for asset in self.__inventory if asset.encrypted]
            self.__rig.storage.extend(movable_assets)
            print(f"All unencrypted assets moved to rig storage.")
            return

        # Store a single named asset
        asset = next((a for a in self.__inventory if a.name == asset_name), None)
        if not asset:
            print(f"{asset_name} not found in {self.__name}'s inventory.")
            return
        if asset.encrypted:
            print(f"{asset_name} is encrypted and cannot be moved.")
            return

        self.__inventory.remove(asset)
        self.__rig.storage.append(asset)
        print(f"{asset_name} moved to rig storage.")

    def retrieve_asset(self, asset_name: str = "", all_items: bool = False):
        if not self.__rig:
            print(f"{self.__name} has no rig to retrieve assets from.")
            return

        if all_items:
            movable_assets = [asset for asset in self.__rig.storage if not asset.encrypted]
            if not movable_assets:
                print(f"No unencrypted assets in {self.__name}'s rig to retrieve.")
                return

            for asset in movable_assets:
                self.__rig.storage.remove(asset)
                self.__inventory.append(asset)

            print(f"{self.__name} retrieved all unencrypted assets ({len(movable_assets)} total).")
            return

        asset = next((asset for asset in self.__rig.storage if asset.name == asset_name), None)
        if not asset:
            print(f"{asset_name} not found in rig storage.")
            return
        if asset.encrypted:
            print(f"{asset_name} is encrypted and cannot be moved.")
            return

        self.__rig.storage.remove(asset)
        self.__inventory.append(asset)
        print(f"{asset_name} moved to {self.__name}'s inventory.")

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

        print(f"{self.__name} extracted {len(unsecured_assets)} unencrypted assets from {target_rig.name}.")

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
        target_rig.take_hit(target_rig.get_level())
        if target_rig.is_broken():
            self.extract_assets(target_rig)
        self.__trace_level += 1

    def scan_inventory(self, asset_name: str):
        asset = next((asset for asset in self.__inventory if asset.name == asset_name), None)
        if asset:
            self.__inventory.remove(asset)
            return asset
        return None

    def __str__(self):
        rig_status = self.__rig.name if self.__rig else "No Rig"
        inv_contents = ", ".join(a.name for a in self.__inventory) or "Empty"
        return (f"Hacker: {self.__name}\n"
                f"Trace Level: {self.__trace_level}/{self.__trace_limit}\n"
                f"Rig: {rig_status}\n"
                f"Inventory: {inv_contents}")
