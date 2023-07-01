#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Function that finds a peak in a list of unsorted integers"""
    if list_of_integers == []:
        return None

    ln = len(list_of_integers)

    if ln == 1:
        return list_of_integers[0]

    if ln == 2:
        return max(list_of_integers)

    mid = ln // 2

    if list_of_integers[mid] >= list_integers[mid - 1]\
            and list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    elif list_of_integers[mid + 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[mid + 1:])
    else:
        return find_peak(list_of_integers[:mid])
