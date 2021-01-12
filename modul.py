# Author    : Relarizky
# Github    : https://github.com/relarizky
# ----------------------------------------
# Copyright © Relarizky 2021


def sum(*number_list: tuple) -> int:
    """
    sum all the given number values
    """

    result = 0

    for number in number_list:
        if not number.isdigit():
            # do not process non-number input
            continue

        result += int(number)

    return result


def multiply(*number_list: tuple) -> int:
    """
    multiply all the given number values each other
    """

    result = 0

    for number in number_list:
        if not number.isdigit():
            # do not process non-number input
            continue
        
        result *= int(number)

    return result
