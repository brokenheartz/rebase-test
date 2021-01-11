#!/usr/bin/env python3
# Author    : Relarizky
# Github    : https://github.com/relarizky
# Copyright © Relarizky 2021


from sys import argv, exit


def sum(*values: tuple) -> int:
    """
    sum all given values
    """

    result = 0

    for value in values:
        if not value.isdigit():
            print("input needs to be number")
            exit(1)

        result += int(value)

    return result


if __name__ == "__main__":
    # executed when user run this file
    user_input = argv[1:]

    if user_input == []:
        print("please provide the input")
        exit(0)

    print(f"the result is\t: {sum(*user_input)}")
