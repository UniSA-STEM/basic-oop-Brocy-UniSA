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
    print(hacker.get_rig())

    # Tests if it can upgrade without item
    hacker.upgrade_rig()
    # I just wanted to see what they output would look like
    # when its level 20+
    for _ in range(5):
        hacker.get_inventory().append(HardwarePatch())
        hacker.upgrade_rig()
        hacker.get_rig().generate_asset()
        hacker.get_rig().generate_asset()
    # Checks what happens when full
    for _ in range(3):
        hacker.get_rig().generate_asset()

    print(hacker.get_rig())


def test_encryption_decryption(hacker):
    """Tests if hacker class can (en/de)crypt an item"""
    print("--------- TEST 3: Encryption and Decryption ---------\n")

    hacker.get_inventory().append(SecurityChip())

    asset_to_encrypt = hacker.get_inventory()[0]
    hacker.encrypt_asset(asset_to_encrypt)
    print(asset_to_encrypt)

    hacker.encrypt_asset(asset_to_encrypt)

    hacker.get_inventory().append(SecurityChip())
    hacker.decrypt_asset(asset_to_encrypt)
    print(asset_to_encrypt)


def test_storage_and_retrieval(hacker):
    """Tests if hacker class can store and retrieve an item"""
    print("--------- TEST 4: Asset Storage and Retrieval ---------\n")
    # Upgrades here to give more space for testing
    for _ in range(5):
        hacker.get_inventory().append(HardwarePatch())
        hacker.upgrade_rig()

    for _ in range(6):
        # tests retrieving one asset from rig
        hacker.retrieve_asset(hacker.get_rig().storage[0].name)
    print(hacker)
    print(hacker.get_rig())

    # tests storing all assets to rig
    hacker.store_asset(all_items=True)
    print(hacker.get_rig())


def test_attack_and_extraction():
    print("-------- TEST 5: Combat, Extraction, and Trace --------\n")
    # creates the attacker and targets
    attacker = Hacker("V")
    target = Hacker("Judy")
    attacker.acquire_rig("Archer Hella EC-D i360")
    target.acquire_rig("Sea Dragon")
    target.get_rig().generate_asset()
    target.get_rig().generate_asset()
    attacker.get_inventory().append(RemovableDrive())

    print(attacker)
    print(attacker.get_rig())
    print(target)
    print(target.get_rig())

    attacker.launch_data_spike(target.get_rig())
    attacker.launch_data_spike(target.get_rig())

    print(target.get_rig())
    print(attacker.get_rig())

    print(attacker)
    attacker.hide()
    print(attacker)


def main():
    print("=== CYBERPUNK HACKER SIMULATION ===")
    sun = test_buy_rig()
    test_upgrade_and_generation(sun)
    test_encryption_decryption(sun)
    test_storage_and_retrieval(sun)
    test_attack_and_extraction()
    print("\n=== Simulation Complete ===")


if __name__ == "__main__":
    main()
