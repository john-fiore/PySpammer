import random as rn
import subprocess as sp
import os
import sys

clr = lambda: os.system("cls" if os.name == "nt" else "clear")  # Works on Windows & Unix

NUMBERS = list(range(10))           # [0-9]
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F']  # HEX letters

def setCol(number: int, letter: str):
    # Validate inputs
    if number not in NUMBERS or letter.upper() not in LETTERS:
        print("Error: Given number or letter not valid!")
        input("Press Enter to exit...")
        sys.exit(1)
    else:
        full = f"{number}{letter.upper()}"
        sp.run(['color', full], shell=True)

def spam(msg: str, amt: int):
    for _ in range(amt):
        print(msg)
    print()
    choice = input("Restart? (y/n): ").lower()
    if choice == "y":
        setCol(0, "F")
        setup()
    else:
        sys.exit(0)

def setup():
    clr()
    print("Welcome!\n")
    print("Would you like to manually set the color or have it randomized?")
    colmode = input("1 for manual, 2 for randomized: ").strip()
    clr()

    if colmode == "1":
        try:
            n = int(input("Pick a number 0-9: ").strip())
            if n not in NUMBERS:
                raise ValueError
            l = input("Pick a letter A-F: ").strip().upper()
            if l not in LETTERS:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter valid number and letter.")
            input("Press Enter to exit...")
            sys.exit(1)
    elif colmode == "2":
        n = rn.choice(NUMBERS)
        l = rn.choice(LETTERS)
    else:
        print("Invalid option.")
        input("Press Enter to exit...")
        sys.exit(1)

    clr()
    msg = input("What is your message: ").strip()
    try:
        amt = int(input("How many times should it loop: ").strip())
    except ValueError:
        print("Invalid number.")
        input("Press Enter to exit...")
        sys.exit(1)

    clr()
    setCol(n, l)
    spam(msg, amt)

if __name__ == "__main__":
    setup()
