#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Function that finds a peak in a list of unsorted integers"""
    ln = len(list_of_integers)

    if ln == 0:
        return None

    mid = ln // 2
    mid_e = ln

    while True:
        mid_e = mid_e // 2

        if mid < ln - 1 and list_of_integers[mid] < list_of_integers[mid + 1]:
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid + mid_e // 2
        elif mid_e > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid - mid_e // 2
        else:
            return list_of_integers[mid]
