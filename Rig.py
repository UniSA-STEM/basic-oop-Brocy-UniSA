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
    def __init__(self, name: str = None):
        self.__name = name if name is not None else "Basic Rig"
        self.__damage = 0
        self.__broken = False
        self.__rig_storage = ["DataSpike", "DataSpike", "RemovableDrive"]
        self.__upgrade_level = 0

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

    def damage_taken(self):
        """Each hit increases damage by 1. If damage reaches 2 (for a level 0 rig), the rig becomes broken"""
        pass

    def generate_assets(self):
        """randomly make 1 asset

        probably use import random, and likely do this in the asset class"""
        pass

    def transfer_storage(self):
        """can transfer items to and from the hacker’s inventory. If an asset is encrypted,
        it cannot be transferred until decrypted"""
        pass

    def rig_info(self):
        """A method should return the rig’s condition based on damage and upgrade level. For example,
        “Pristine (Level 2)” or “Broken (Level 0)”."""
        pass

    def __str__(self):
        """Return a string representation of the Rig."""
        pass
