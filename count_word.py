#!/usr/bin/env python
# coding=utf-8

"""
Find the top 10 word in file
Usage:
python count_word.py file.txt
"""
import sys
import re
from collections import Counter


def main():
    if len(sys.argv) < 2:
        print __doc__
        sys.exit(1)

    # open the file and readin as str
    with open(sys.argv[1]) as f:
        context = f.read()

    # split the str into words
    word_list = Counter(re.split('\W+', context))
    print word_list.most_common(10)


if __name__ == '__main__':
    main()
