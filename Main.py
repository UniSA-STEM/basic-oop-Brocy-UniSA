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
    """Tests if hacker class can buy a rig, and if it consumes the item"""
    print("\n--- TEST 1: Rig Purchase ---")
    neo = Hacker("NeoShadow")
    print(neo)
    neo.acquire_rig()
    print(neo)
    return neo

def main():
    print("=== CYBERPUNK HACKER SIMULATION ===")
    neo = test_buy_rig()
    print("\n=== Simulation Complete ===")


if __name__ == "__main__":
    main()
