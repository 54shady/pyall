#!/usr/bin/env python
# coding=utf-8


def bubble_sort(ARRAY):
    length = len(ARRAY)
    for i in range(length-1):
        swapped = False
        for j in range(length-1-i):
            if ARRAY[j] > ARRAY[j+1]:
                swapped = True
                ARRAY[j], ARRAY[j+1] = ARRAY[j+1], ARRAY[j]
        if not swapped:
            break  # Stop iteration if the ARRAY is sorted.
    return ARRAY


if __name__ == '__main__':
    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print bubble_sort(unsorted)
