#!/usr/bin/env python
# coding=utf-8

class DemoCls(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v) # self.k = v

    def get_cls_attr(self, key_name):
        print getattr(self, key_name)

    def has_attr(self, key_name):
        return hasattr(self, key_name)

def main():
    dcls = DemoCls(
            key1="value1",
            key2="value2",
            key3="value3")

    if dcls.has_attr("key1") :
        dcls.get_cls_attr("key1")

    if dcls.has_attr("key2"):
        dcls.get_cls_attr("key2")

    if dcls.has_attr("key3"):
        dcls.get_cls_attr("key3")

    if dcls.has_attr("key4"):
        dcls.get_cls_attr("key4")

if __name__ == '__main__':
    main()
