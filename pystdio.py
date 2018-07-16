#!/usr/bin/env python
# coding=utf-8

import sys

""" usage
cat a_file | python pystdio.py
:!cat a_file | python %
"""


def main():
    # read from stdin
    lines = sys.stdin.readlines()

    # print out the data
    for i in range(len(lines)):
        line = lines[i].rstrip()
        print line


if __name__ == '__main__':
    main()
