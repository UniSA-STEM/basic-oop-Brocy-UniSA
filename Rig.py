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
        self.__rig_storage = []

    @property
    def storage(self):
        return self.__rig_storage

    @storage.setter
    def storage(self, item):
        pass