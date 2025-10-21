"""
File: Hacker.py
Description: Defines the Hacker class, which manages a hacker's rig,
inventory, and actions like encryption, extraction, and digital combat.
Author: Corey Brooke
ID: 110480857
Username: Brocy076
This is my own work as defined by the
University's Academic Misconduct Policy.
"""
from Asset import *
from Rig import Rig


class Hacker:
    """
    Attributes:
        __name (str): Hacker's unique alias.
        __trace_level (int): Current trace risk; increases after risky
        actions.
        __trace_limit (int): Maximum allowed trace before being
        exposed.
        __rig (Rig | Default: None): The hacker's assigned rig, if any.
        __inventory (list[Asset]): Items currently carried by the
        hacker.
        __max_inventory (int): Maximum capacity of the hacker's
        inventory.
    """

    def __init__(self, name: str):
        """
        Initialize the hacker with a name, one CryptoToken, and no rig.
        """
        self.__name = name
        self.__trace_level = 0
        self.__trace_limit = 5
        self.__rig = None
        self.__inventory = [CryptoToken()]
        self.__max_inventory = 5

    def acquire_rig(self, rig: str | None = None):
        """
        Acquire a new rig using one CryptoToken, using it if they have
        it. The hacker than receives a rig.
        """
        # Searches for the first case of an asset in the inventory
        token = next((asset for asset in self.__inventory if
                      asset.name == "CryptoToken"), None)
        if not token:
            print(
                f"{self.__name} doesn’t have enough CryptoTokens to "
                f"buy a rig.")
            return

        self.__inventory.remove(token)

        # If a rig name was given then they are given it will pass that
        # through, with the hackers name.
        self.__rig = Rig(rig, owner=self.__name)
        print(
            f"{self.__name}, your rig is activated and ready for use.")

    def upgrade_rig(self):
        """
        Upgrade the Hacker's Rig using a HardwarePatch from inventory
        """
        if not self.__rig:
            print(f"{self.__name} has no rig to upgrade.")
            return
        self.__rig.upgrade(self.__inventory)

    def encrypt_asset(self, asset: Asset):
        """
        Encrypt a given asset using a SecurityChip by calling the
        encryption method from Asset class.
        """
        chip = next((asset for asset in self.__inventory if
                     asset.name == "SecurityChip"), None)
        if not chip:
            print(
                "There are no SecurityChips in inventory for "
                "encryption.")
            return
        if asset.encrypted:
            print(f"{asset.name} has already been encrypted.")
            return

        self.__inventory.remove(chip)
        asset.encrypt()
        print(f"{asset.name} encrypted.")

    def decrypt_asset(self, asset: Asset):
        """
        Decrypt a given asset using a SecurityChip by calling the
        decryption method from Asset class.
        """
        chip = next((asset for asset in self.__inventory if
                     asset.name == "SecurityChip"), None)
        if not chip:
            print("There are no SecurityChips in inventory for "
                  "decryption.")
            return
        if not asset.encrypted:
            print(f"{asset.name} is not encrypted.")
            return

        self.__inventory.remove(chip)
        asset.decrypt()
        print(f"{asset.name} decrypted.")

    def store_asset(self, asset_name: str = "", all_items: bool = False):
        """
        Move one or all unencrypted assets from the hacker's
        inventory to their rig's storage, without going over the
        Rig's storage limit.
        """
        if not self.__rig:
            print(f"{self.__name} has no rig to store assets in.")
            return

        max_storage = self.__rig.get_max_storage()
        current_storage = len(self.__rig.storage)

        if all_items:
            # Checks if items are encrypted and puts the ones that are into
            # a new list
            movable_assets = [asset for asset in self.__inventory if
                              not asset.encrypted]
            if not movable_assets:
                print("No movable (unencrypted) assets found in "
                      "inventory.")
                return

            available_slots = max_storage - current_storage
            if available_slots <= 0:
                print(
                    f"{self.__rig.name}'s storage is full ("
                    f"{max_storage} max). Cannot move any assets.")
                return

            # Move as many assets as will fit in Rig storage.
            assets_to_move = movable_assets[:available_slots]
            for asset in assets_to_move:
                self.__inventory.remove(asset)
                self.__rig.storage.append(asset)

            print(
                f"{len(assets_to_move)} unencrypted assets moved to "
                f"rig storage ({len(self.__rig.storage)}/"
                f"{max_storage}).")
            return

        # If all_items is False then it will only move one item.
        asset = next(
            (asset for asset in self.__inventory if asset.name == asset_name),
            None)
        if not asset:
            print(
                f"{asset_name} not found in {self.__name}'s inventory.")
            return
        if asset.encrypted:
            print(f"{asset_name} is encrypted and cannot be moved.")
            return
        if current_storage >= max_storage:
            print(
                f"{self.__rig.name}'s storage is full ({max_storage} "
                f"max).")
            return

        self.__inventory.remove(asset)
        self.__rig.storage.append(asset)
        print(f"{asset_name} moved to rig storage "
              f"({len(self.__rig.storage)}/{max_storage}).")

    def retrieve_asset(self, asset_name: str = "", all_items: bool = False):
        """
        Retrieve one or all unencrypted assets from the rig's storage
        back to the hacker's inventory, without going over the
        Hacker's inventory limit.
        """
        if not self.__rig:
            print(f"{self.__name} has no rig to retrieve assets from.")
            return

        max_inventory = 5
        current_inventory = len(self.__inventory)

        if all_items:
            movable_assets = [asset for asset in self.__rig.storage if
                              not asset.encrypted]
            if not movable_assets:
                print(
                    f"No unencrypted assets in {self.__name}'s rig to "
                    f"retrieve.")
                return

            available_slots = max_inventory - current_inventory
            if available_slots <= 0:
                print(f"{self.__name}'s inventory is full ("
                      f"{max_inventory} max).")
                return

            # Move as many assets as fit in inventory
            assets_to_move = movable_assets[:available_slots]
            for asset in assets_to_move:
                self.__rig.storage.remove(asset)
                self.__inventory.append(asset)

            print(
                f"{self.__name} retrieved {len(assets_to_move)} "
                f"unencrypted assets ({len(self.__inventory)}/"
                f"{max_inventory} inventory slots used).")
            return

        # If all_items is False then it will only move one item.
        asset = next((asset for asset in self.__rig.storage if
                      asset.name == asset_name), None)
        if not asset:
            print(f"{asset_name} not found in rig storage.")
            return
        if asset.encrypted:
            print(f"{asset_name} is encrypted and cannot be moved.")
            return
        if current_inventory >= max_inventory:
            print(
                f"{self.__name}'s inventory is full ({max_inventory} "
                f"max).")
            return

        self.__rig.storage.remove(asset)
        self.__inventory.append(asset)
        print(f"{asset_name} moved to {self.__name}'s inventory "
              f"({len(self.__inventory)}/{max_inventory}).")

    def extract_assets(self, target_rig: Rig):
        """
        Extract unencrypted assets from a broken rig using a
        RemovableDrive (Consuming it), and transfer unencrypted
        assets to the hacker's inventory, without going over the limit.
        """
        drive = next((asset for asset in self.__inventory if
                      asset.name == "RemovableDrive"), None)
        if not drive:
            print(
                "There are no RemovableDrives, unable to complete "
                "extraction.")
            return

        self.__inventory.remove(drive)

        unsecured_assets = [asset for asset in target_rig.storage if
                            not asset.encrypted]
        if not unsecured_assets:
            print(
                f"No unencrypted assets found in {target_rig.name}. "
                f"Nothing to extract.")
            return

        max_inventory = 5
        available_slots = max_inventory - len(self.__inventory)
        if available_slots <= 0:
            print(
                f"{self.__name}'s inventory is full ({max_inventory} "
                f"max). Cannot extract any assets.")
            return

        # Move as many assets as fit in inventory
        assets_to_extract = unsecured_assets[:available_slots]
        for asset in assets_to_extract:
            self.__inventory.append(asset)
            target_rig.storage.remove(asset)

        extracted_count = len(assets_to_extract)
        total_unencrypted = len(unsecured_assets)
        if extracted_count < total_unencrypted:
            print(
                f"{self.__name} extracted {extracted_count}/"
                f"{total_unencrypted} assets before inventory reached "
                f"its limit ({len(self.__inventory)}/{max_inventory}).")
        else:
            print(
                f"{self.__name} successfully extracted all "
                f"{extracted_count} unencrypted assets from "
                f"{target_rig.name}.")

    def launch_data_spike(self, target_rig: Rig):
        """
        Attack another rig using a DataSpike from the hacker's rig
        storage (Consuming it), with each successful hit increases
        the target rig's damage and raises the hacker's trace level.
        If the target rig breaks, unsecured assets are extracted
        automatically.
        """
        if not self.__rig:
            print("No rig available to launch attack.")
            return
        if self.__trace_level >= self.__trace_limit:
            print(
                f"{self.__name} is exposed and cannot attack until "
                f"trace level is reduced!")
            return

        spike = next((asset for asset in self.__rig.storage if
                      asset.name == "DataSpike"), None)
        if not spike:
            print("There are no DataSpikes available in storage to "
                  "launch attack.")
            return

        self.__rig.storage.remove(spike)
        target_rig.take_hit(target_rig.get_level())
        if target_rig.is_broken():
            self.extract_assets(target_rig)
        self.__trace_level += 1  # Each attack increases trace risk.

    def scan_inventory(self, asset_name: str):
        """
        Scan for and remove a specific asset from the hacker's
        inventory.
        """
        asset = next(
            (asset for asset in self.__inventory if asset.name == asset_name),
            None)
        if asset:
            self.__inventory.remove(asset)
            return asset
        return None

    def __str__(self):
        """Return a formatted summary of the hacker's current state."""
        rig_status = self.__rig.name if self.__rig else "No Rig"
        inv_contents = ", ".join(
            asset.name for asset in self.__inventory) or "Empty"

        lines = [
            f"Hacker: {self.__name}",
            f"Trace Level: {self.__trace_level}/{self.__trace_limit}",
            f"Rig: {rig_status}",
            f"Inventory: {inv_contents}",
        ]

        max_length = max(len(line) for line in lines)
        horizontal_border = "+" + "-" * (max_length + 2) + "+"

        boxed_lines = [horizontal_border]
        for line in lines:
            boxed_lines.append(f"| {line.ljust(max_length)} |")
        boxed_lines.append(horizontal_border)

        return "\n".join(boxed_lines)
