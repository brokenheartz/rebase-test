#!/usr/bin/env python3
# Author    : Relarizky
# Github    : https://github.com/relarizky
# Copyright © Relarizky 2021


from sys import argv
from modul import sum


if __name__ == "__main__":
    # executed when user run this file
    user_input = argv[1:]

    print(f"the sum result is\t: {sum(*user_input)}")
