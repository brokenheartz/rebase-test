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


def largest(*number_list: tuple) -> int:
    """
    find the largest number amongst the input list
    """
    
    # eliminate non-number value in number_list
    number_list = filter(
        lambda element: element.isdigit(),
        number_list
    )

    # do type-casting to all the elements
    number_list = map(
        lambda element: int(element),
        number_list
    )

    # do type-casting from map object to list
    number_list = list(number_list)

    # sort the number_list
    for count in range(len(number_list)):
        for index in range(len(number_list)-1):
            if number_list[index] > number_list[index+1]:
                temp = number_list[index]
                number_list[index] = number_list[index+1]
                number_list[index+1] = temp

    return number_list[-1] if number_list != [] else 0
