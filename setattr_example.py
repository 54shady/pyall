#!/usr/bin/env python
# coding=utf-8

class DemoCls(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v) # self.k = v

def main():
    dcls = DemoCls(
            key1="value1",
            key2="value2",
            key3="value3")

    print dcls.key1
    print dcls.key2
    print dcls.key3

if __name__ == '__main__':
    main()
