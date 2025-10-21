"""
File: main.py
Description: Runs demonstrations and tests for the classes:
    - Asset
    - Rig
    - Hacker
Author: Corey Brooke
ID: 110480857
Username: Brocy076
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import *
from Rig import Rig
from Hacker import Hacker


def test_buy_rig():
    """
    Tests if hacker class can buy a rig, and if it consumes the item
    """
    print("----------------- TEST 1: Rig Purchase -----------------\n")
    neo = Hacker("NeoShadow")
    print(neo)
    neo.acquire_rig()
    print(neo)

    sun = Hacker("Sun_Rider")
    print(sun)
    sun.acquire_rig("StarShip") # to see if the custom names work
    print(sun)
    return sun


def test_upgrade_and_generation(hacker):
    """
    Tests if hacker class can upgrade an item, and if it
    consumes the item
    """
    print("--------- TEST 2: Upgrade and Asset Generation ---------\n")

    print(hacker)
    print(hacker._Hacker__rig)

    # Tests if it can upgrade without item
    hacker.upgrade_rig()
    # I just wanted to see what they output would look like
    # when its level 20+
    for _ in range(5):
        hacker._Hacker__inventory.append(HardwarePatch())
        hacker.upgrade_rig()
        hacker._Hacker__rig.generate_asset()
        hacker._Hacker__rig.generate_asset()
    # Checks what happens when full
    for _ in range(3):
        hacker._Hacker__rig.generate_asset()

    print(hacker._Hacker__rig)


def main():
    print("=== CYBERPUNK HACKER SIMULATION ===")
    sun = test_buy_rig()
    test_upgrade_and_generation(sun)
    print("\n=== Simulation Complete ===")


if __name__ == "__main__":
    main()
