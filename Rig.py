"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Corey Brooke
ID: 110480857
Username: Brocy076
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random
from Asset import *


class Rig:
    def __init__(self, name: str = None, owner=None):
        self.__name = name if name is not None else "Basic Rig"
        self.__damage = 0
        self.__broken = False
        self.__rig_storage = [DataSpike(), DataSpike(), RemovableDrive()]
        self.__upgrade_level = 0
        self.__owner = owner

    @property
    def storage(self):
        return self.__rig_storage

    @property
    def name(self):
        return self.__name

    def repair(self):
        """uses Crypto Token to repair the Rig"""
        if self.__damage == 0:
            print("No repair is needed for this Rig")
        else:
            self.__damage = 0
            self.__broken = False
            # TODO Remove DATASPIKE ITEM

    def upgrade(self, hacker_inventory: list):
        patch = next((asset for asset in hacker_inventory if asset.name == "HardwarePatch"), None)
        if not patch:
            print("There are no HardwarePatches available to upgrade rig.")
            return

        hacker_inventory.remove(patch)
        self.__upgrade_level += 1
        print(f"{self.__name} had upgraded their rig \"{self.__name}\" to Level {self.__upgrade_level}!")

    def generate_asset(self):
        asset_classes = [CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch]
        new_asset = random.choice(asset_classes)()
        self.__rig_storage.append(new_asset)
        print(f"Asset: {new_asset.name}, has been generated.")

    def take_hit(self):
        if self.__broken:
            print(f"{self.__name} is already broken.")
            return

        threshold = 2 + self.__upgrade_level
        self.__damage += 1

        if self.__damage >= threshold:
            self.__broken = True
            print(f"{self.__owner}'s Rig \"{self.__name}\" has broken under attack!")
        else:
            print(f"{self.__name} took damage ({self.__damage}/{threshold}).")

    def generate_assets(self):
        """randomly make 1 asset

        probably use import random, and likely do this in the asset class"""
        pass

    def rig_info(self):
        """A method should return the rig’s condition based on damage and upgrade level. For example,
        “Pristine (Level 2)” or “Broken (Level 0)”."""
        pass

    def __str__(self):
        """Return a string representation of the Rig."""
        pass
