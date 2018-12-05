#!/usr/bin/env python
# coding=utf-8

"""
This is a pure python implementation of the quick sort algorithm

For doctests run following command:
python -m doctest -v quick_sort.py
or
python3 -m doctest -v quick_sort.py

For manual testing run:
python quick_sort.py
"""
import random
import sys


def median3(ARRAY):
    """
    return the middle valeu of (ARRAY[0], ARRAY[mid], ARRAY[len-1])
    """
    left_mid_right = []
    left_index = 0
    right_index = len(ARRAY) - 1
    mid_index = (left_index + right_index) / 2
    left_mid_right.append(ARRAY[left_index])
    left_mid_right.append(ARRAY[mid_index])
    left_mid_right.append(ARRAY[right_index])
    left_mid_right.sort()
    # return middle value
    return left_mid_right[1]


def get_pivot(ARRAY):
    global pivot_flag
    if pivot_flag == 0:
        # random pivot
        index = random.randint(0, len(ARRAY)-1)
        return ARRAY[index]
    else:
        # median 3 pivot
        return median3(ARRAY)


def quick_sort(ARRAY):
    """
    将数组S快速排序的4个步骤
    1. 如果S中的元素个数为0或1,返回
    2. 取S中任意一个元素作为pivot
    3. 将剩余元素分成两个不相交的集合S1(小于pivot), S2(大于pivot)
    4. 返回quick_sort(S1), 再放回pivot, 最后返回quick_sort(S2)

    pivot选取原则
    方法1. 比较安全的方针是随机选取
    方法2. 3数中值分割法
        pivot 取最左,中间,最右三个数中的中间值
        pivot = mid(S[0], S[mid], S[len(S)-1])
    """
    if len(ARRAY) <= 1:
        return ARRAY
    else:
        # get pivot
        PIVOT = get_pivot(ARRAY)
        # split the left number into two division
        ARRAY.remove(PIVOT)
        GREATER = [element for element in ARRAY if element > PIVOT]
        LESSER = [element for element in ARRAY if element <= PIVOT]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)


if __name__ == '__main__':
    global pivot_flag
    if len(sys.argv) < 2:
        pivot_flag = 0
    elif sys.argv[1] == "-r":
        pivot_flag = 0
    elif sys.argv[1] == "-m":
        pivot_flag = 1
    else:
        pivot_flag = 0

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print quick_sort(unsorted)
