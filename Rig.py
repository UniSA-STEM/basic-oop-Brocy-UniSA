"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Corey Brooke
ID: 110480857
Username: Brocy076
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Hacker import Hacker


class Rig:
    def __init__(self, name: str = None, owner = None):
        self.__name = name if name is not None else "Basic Rig"
        self.__damage = 0
        self.__broken = False
        self.__rig_storage = ["DataSpike", "DataSpike", "RemovableDrive"]
        self.__upgrade_level = 0
        self.__owner = owner

    @property
    def storage(self):
        return self.__storage

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

    def upgrade(self):
        """Increses the rigs upgrade level at the cost of a hardware patch

        upgrades increase battle damage, storage ammount and damage mitigation"""
        self.__upgrade_level += 1

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
