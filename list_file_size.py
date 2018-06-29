#!/usr/bin/env python
# coding=utf-8

import operator, os, sys

# get the file size
def get_file_size(filename):
  st = os.lstat(filename)
  return st.st_size;

def main(argv):
    # the result value
    output = []

    # argv[1:] specify the path need to be statistic
    pathes = argv[1:]

    # walk through all the given pathes
    for path in pathes:
        # walk through the path
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                # absolute file name
                afn = os.path.abspath(os.path.join(dirpath, f))

                # printout format
                record = (
                    get_file_size(afn),
                    os.path.join(dirpath, f))

                # add to output
                output.append(record)

    for record in output:
        print "%12d %s" % record

'''
Description : statistic the file size under given directory
Usage : python list_file_size.py /statistic/path1 /statistic/path2
'''
if __name__ == '__main__':
  main(sys.argv)
