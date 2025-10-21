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
    sun.acquire_rig("StarShip")  # to see if the custom names work
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


def test_encryption_decryption(hacker):
    """Tests if hacker class can (en/de)crypt an item"""
    print("--------- TEST 3: Encryption and Decryption ---------\n")

    hacker._Hacker__inventory.append(SecurityChip())

    asset_to_encrypt = hacker._Hacker__inventory[0]
    hacker.encrypt_asset(asset_to_encrypt)
    print(asset_to_encrypt)

    hacker.encrypt_asset(asset_to_encrypt)

    hacker._Hacker__inventory.append(SecurityChip())
    hacker.decrypt_asset(asset_to_encrypt)
    print(asset_to_encrypt)


def test_storage_and_retrieval(hacker):
    """Tests if hacker class can store and retrieve an item"""
    print("--------- TEST 4: Asset Storage and Retrieval ---------\n")
    # Upgrades here to give more space for testing
    for _ in range(5):
        hacker._Hacker__inventory.append(HardwarePatch())
        hacker.upgrade_rig()


    for _ in range(6):
        # tests retrieving one asset from rig
        hacker.retrieve_asset(hacker._Hacker__rig.storage[0].name)
    print(hacker)
    print(hacker._Hacker__rig)

    # tests storing all assets to rig
    hacker.store_asset(all_items=True)
    print(hacker._Hacker__rig)


def main():
    print("=== CYBERPUNK HACKER SIMULATION ===")
    sun = test_buy_rig()
    test_upgrade_and_generation(sun)
    test_encryption_decryption(sun)
    test_storage_and_retrieval(sun)
    print("\n=== Simulation Complete ===")


if __name__ == "__main__":
    main()
