#!/usr/bin/env python
# coding=utf-8


class Demo1():
    def __len__(self):
        return 9

    def __iter__(self):
        yield "aaa"
        yield "bbb"
        yield "ccc"

    def __getitem__(self, key):
        return list(self)[key]


class Demo2():
    def __init__(self):
        self.list = [11, "AA", "C"]

    def __len__(self):
        return 9

    def __iter__(self):
        """
        make class iterable
        """
        yield "aaa"
        yield "bbb"
        yield "ccc"

    def __getitem__(self, key):
        """
        instance[key] will trigger this function
        """
        return self.list[key]


def main():
    d = Demo1()

    # test __len__
    print "Demo 1 len = %d" % len(d)

    # test __iter__
    print '-' * 30
    gd = iter(d)
    print next(gd)
    print next(gd)
    print next(gd)

    # test __getitem__
    print '-' * 30
    print d[0]
    print d[1]
    print d[2]

    d = Demo2()

    # test __len__
    print "Demo 2 len = %d" % len(d)

    # test __iter__
    print '-' * 30
    gd = iter(d)
    print next(gd)
    print next(gd)
    print next(gd)

    # test __getitem__
    print '-' * 30
    print d[0]
    print d[1]
    print d[2]


if __name__ == '__main__':
    main()
