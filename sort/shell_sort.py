#!/usr/bin/env python
# coding=utf-8

"""
This is a pure python implementation of the shell sort algorithm

For doctests run following command:
python -m doctest -v shell_sort.py
or
python3 -m doctest -v shell_sort.py

For manual testing run:
python shell_sort.py
"""
from __future__ import print_function


def shell_sort(ARRAY):
    # Marcin Ciura's gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    # Start with the largest gap and work down to a gap of 1
    for gap in gaps:
        # Do a gapped insertion sort for this gap size.
        # The first gap elements ARRAY[0..gap-1] are already in gapped order
        # keep adding one more element until the entire array is gap sorted
        i = gap
        while i < len(ARRAY):
            # add ARRAY[i] to the elements that have been gap sorted
            # save ARRAY[i] in temp and make a hole at position i
            temp = ARRAY[i]

            # shift earlier gap-sorted elements up
            # until the correct location for ARRAY[i] is found
            j = i
            while j >= gap and ARRAY[j - gap] > temp:
                ARRAY[j] = ARRAY[j - gap]
                j -= gap

            # put temp (the original ARRAY[i]) in its correct location
            ARRAY[j] = temp
            i += 1

    return ARRAY


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(shell_sort(unsorted))
