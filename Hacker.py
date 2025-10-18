"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Corey Brooke
ID: 110480857
Username: Brocy076
This is my own work as defined by the University's Academic Misconduct Policy.
"""
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
        self.__inventory = ["CryptoToken"]  # TODO: Make the inventory better. (this is just a placeholder)
        self.__rig = None

    def acquire_rig(self, rig=None):
        """
        This function is used to give a rig to the Hacker.

        If the hacker has a CryptoToken, it is removed from the inventory and
        a rig is set, while telling the user that it is activated.
        If the user doesn't have enough tokens a message is printed indicating such.
        """
        if "CryptoToken" in self.__inventory:
            self.__inventory.remove("CryptoToken")
            self.__rig = rig if rig else Rig()
            print(f"{self.__name}, your rig is activated and ready for use.")
        else:
            print(f"{self.__name} doesn’t have enough CryptoTokens to buy a rig.")

    def __str__(self):
        """Return a string representation of the Hacker."""
        rig_status = self.__rig if self.__rig else "No Rig"
        return f"Hacker: {self.__name}\nInventory: {self.__inventory}\nRig: {rig_status}"
