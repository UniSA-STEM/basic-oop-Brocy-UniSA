"""
File: Rig.py
Description: This class represents a Rig (computer) object,
that is used by a Hacker.
Author: Corey Brooke
ID: 110480857
Username: Brocy076
This is my own work as defined by the
University's Academic Misconduct Policy.
"""
from random import choice

from Asset import *


class Rig:
    """
    Represents a digital Rig that stores assets, can be upgraded,
    take damage, and be repaired.

    Attributes:
        __name (str): The name of the Rig.
        __damage (int): The current damage level of the Rig.
        __broken (bool): Whether the Rig is broken and unusable.
        __rig_storage (list[Asset]): The list of assets stored on the
        Rig.
        __upgrade_level (int): The current upgrade level of the Rig.
        __owner (str): The name of the hacker who owns this Rig.
        __max_storage (int): The maximum number of assets the Rig can
        hold.
        """

    def __init__(self, name: str = None, owner=None):
        """
        Initialize the Rig with a default name, owner, and
        starting assets.
        """
        self.__name = name if name is not None else "Basic Rig"
        self.__damage = 0
        self.__broken = False
        self.__rig_storage = [DataSpike(), DataSpike(), RemovableDrive()]
        self.__upgrade_level = 0
        self.__owner = owner
        self.__max_storage = 5

    @property
    def name(self):
        """Return the name of the Rig."""
        return self.__name

    @property
    def storage(self):
        """Return the list of assets currently stored on the Rig."""
        return self.__rig_storage

    def get_max_storage(self):
        return self.__max_storage

    def get_level(self):
        return self.__upgrade_level

    def upgrade(self, hacker_inventory: list):
        """
        Upgrade the Rig using a HardwarePatch from the hacker's
        inventory (Consuming it). Each upgrade increases the Rig's
        level and expands storage capacity.
        """
        patch = next((asset for asset in hacker_inventory if
                      asset.name == "HardwarePatch"), None)
        if not patch:
            print(
                "There are no HardwarePatches available to upgrade "
                "Rig.")
            return

        hacker_inventory.remove(patch)
        self.__upgrade_level += 1  # Adds one level to Rig
        # Starts at 5 storage and adds 2 per level
        self.__max_storage = 5 + (
                self.__upgrade_level * 2)
        print(
            f"{self.__name} had upgraded their Rig \"{self.__name}\" to"
            f" Level {self.__upgrade_level}!")

    def generate_asset(self):
        """
        Randomly generate a new asset and add it to the Rig's storage
        if the storage isn't full.
        """
        if len(self.__rig_storage) >= self.__max_storage:
            print(
                f"{self.__name}'s storage is full! Cannot generate new"
                f" assets.")
            return

        # Sets the possible options (all the subclasses from Asset) and
        # randomly chooses one
        asset_classes = [CryptoToken, DataSpike, RemovableDrive, SecurityChip,
                         HardwarePatch]
        new_asset = choice(asset_classes)()
        self.__rig_storage.append(new_asset)
        print(
            f"Asset: {new_asset.name}, has been generated and added to"
            f" storage.")

    def take_hit(self, attacking_rig_level):
        """
        Calculate how much damage the Rig takes based on both Rig's
        level, If the accumulated damage exceeds the Rig's threshold,
        it becomes broken.
        """
        if self.__broken:
            print(f"{self.__name} is already broken.")
            return

        threshold = 2 + self.__upgrade_level  # Basic Rig brakes at 2
        self.__damage += (1 + attacking_rig_level)

        if self.__damage >= threshold:
            self.__broken = True
            print(
                f"{self.__owner}'s Rig \"{self.__name}\" has broken "
                f"under attack!")
        else:
            print(
                f"{self.__name} took damage ({self.__damage}/"
                f"{threshold}).")

    def repair(self, hacker_inventory: list):
        """
        Repair the rig using a CryptoToken from the hacker's inventory
        (Consuming it), and fully restores the rig's condition
        and removes all damage
        """
        token = next((asset for asset in hacker_inventory if
                      asset.name == "CryptoToken"), None)
        if not token:
            print(
                f"{self.__owner} doesn’t have enough CryptoTokens to "
                f"repair {self.__name}.")
            return
        if self.__damage == 0:
            print(f"{self.__name} doesn't need repairs.")
            return
        hacker_inventory.remove(token)
        self.__damage = 0
        self.__broken = False
        print(f"{self.__owner} has repaired \"{self.__name}\".")

    def condition(self):
        """Return string showing the rig's condition and level"""
        if self.__broken:
            return f"Broken (Level {self.__upgrade_level})"
        elif self.__damage == 0:
            return f"Pristine (Level {self.__upgrade_level})"
        return f"Damaged (Level {self.__upgrade_level})"

    def is_broken(self):
        """Return True if the rig is broken, otherwise return False."""
        return self.__broken

    def __str__(self):
        """
        Return a formatted string summarizing the rig's status and
        stored assets.
        """
        stored_assets = ", ".join(
            asset.name for asset in self.__rig_storage) or "Empty"
        return (f"Rig: {self.__name} | {self.condition()} | Assets: "
                f"{stored_assets}")
