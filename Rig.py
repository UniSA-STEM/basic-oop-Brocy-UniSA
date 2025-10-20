"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Corey Brooke
ID: 110480857
Username: Brocy076
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from random import choice

from Asset import *


class Rig:
    def __init__(self, name: str = None, owner=None):
        self.__name = name if name is not None else "Basic Rig"
        self.__damage = 0
        self.__broken = False
        self.__rig_storage = [DataSpike(), DataSpike(), RemovableDrive()]
        self.__upgrade_level = 0
        self.__owner = owner
        self.__max_storage = 5

    @property
    def storage(self):
        return self.__rig_storage

    @property
    def name(self):
        return self.__name

    def upgrade(self, hacker_inventory: list):
        patch = next((asset for asset in hacker_inventory if asset.name == "HardwarePatch"), None)
        if not patch:
            print("There are no HardwarePatches available to upgrade rig.")
            return

        hacker_inventory.remove(patch)
        self.__upgrade_level += 1
        self.__max_storage = 5 + (self.__upgrade_level * 2)
        print(f"{self.__name} had upgraded their rig \"{self.__name}\" to Level {self.__upgrade_level}!")

    def get_level(self):
        return self.__upgrade_level

    def get_max_storage(self):
        return self.__max_storage

    def generate_asset(self):
        if len(self.__rig_storage) >= self.__max_storage:
            print(f"{self.__name}'s storage is full! Cannot generate new assets.")
            return

        asset_classes = [CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch]
        new_asset = choice(asset_classes)()
        self.__rig_storage.append(new_asset)
        print(f"Asset: {new_asset.name}, has been generated and added to storage.")

    def take_hit(self, attacking_rig_level):
        if self.__broken:
            print(f"{self.__name} is already broken.")
            return

        threshold = 2 + self.__upgrade_level
        self.__damage += (1 + attacking_rig_level)

        if self.__damage >= threshold:
            self.__broken = True
            print(f"{self.__owner}'s Rig \"{self.__name}\" has broken under attack!")
        else:
            print(f"{self.__name} took damage ({self.__damage}/{threshold}).")

    def repair(self, hacker_inventory: list):
        token = next((asset for asset in hacker_inventory if asset.name == "CryptoToken"), None)
        if not token:
            print(f"{self.__owner} doesn’t have enough CryptoTokens to repair {self.__name}.")
            return
        if self.__damage == 0:
            print(f"{self.__name} doesn't need repairs.")
            return
        hacker_inventory.remove(token)
        self.__damage = 0
        self.__broken = False
        print(f"{self.__owner} has repaired \"{self.__name}\".")

    def condition(self):
        if self.__broken:
            return f"Broken (Level {self.__upgrade_level})"
        elif self.__damage == 0:
            return f"Pristine (Level {self.__upgrade_level})"
        return f"Damaged (Level {self.__upgrade_level})"

    def is_broken(self):
        return self.__broken

    def __str__(self):
        stored_assets = ", ".join(asset.name for asset in self.__rig_storage) or "Empty"
        return f"Rig: {self.__name} | {self.condition()} | Assets: {stored_assets}"
