"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Corey Brooke
ID: 110480857
Username: Brocy076
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Hacker import Hacker
from Rig import Rig

class Asset():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.encrypted = False

    def transfer(self):
        """Changes the inventory it is stored in

        something like if its in one move to other, but i will need a class to check what one it is in"""
        pass


    def __str__(self):
        """Return a string representation of the Asset."""
        pass
