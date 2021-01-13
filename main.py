#!/usr/bin/env python3
# Author    : Relarizky
# Github    : https://github.com/relarizky
# ----------------------------------------
# Copyright © Relarizky 2021


from sys import argv
from modul import sum, multiply, first_last


if __name__ == "__main__":
    # executed when user run this file
    user_input = argv[1:]

    print(f"the sum result is\t: {sum(*user_input)}")
    print(f"the largest value is\t: {first_last(*user_input, first=False)}")
    print(f"the smallest value is\t: {first_last(*user_input)}")
    print(f"the multiply result is\t: {multiply(*user_input)}")
