#!/usr/bin/env python
# coding=utf-8

import sys

""" Load 'key=value' pairs from filename """
def parse_kv_file(filename):
    record = {}
    f = open(filename)

    # parse each line in file
    for line in f:
        # trim the leading and trialing white space
        line = line.strip()

        # filter out blank and comment line
        if not line or line.startswith('#'):
            continue

        key, value = line.split('=', 1)
        record[key] = value

    # close the file
    f.close()

    return record

""" traversal the dictionary """
def traversal(d):
    for k in d:
        print '%s=%s' % (k, d[k])

if __name__ == '__main__':
    # parse the KeyValue pair file
    d = parse_kv_file(sys.argv[1])

    # print out the KeyValue pairs
    traversal(d)
