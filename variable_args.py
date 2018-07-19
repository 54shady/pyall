#!/usr/bin/env python
# coding=utf-8


def traversal(d):
    """ traversal the dictionary """
    for k in d:
        print '%s=%s' % (k, d[k])


class Baz():
    def __init__(self, **kwargs):
        print 'Baz init...'
        traversal(kwargs)


def bar(**kwargs):
    print 'bar is being called'
    traversal(kwargs)


def foo(var1=None, var2=None, **kwargs):
    if var1 is None:
        # call a method
        bar(**kwargs)
    elif var2 is None:
        # call a class
        Baz(**kwargs)
    else:
        print 'Either var1 or var2 is None'
        pass


def main():
    foo(var1=1, var2=2, new1=3, new2=4)

    print '-' * 30
    foo(var2=22, new1=1, new2=2)

    print '-' * 30
    foo(var1=1, new3=3, new4=4, new5=5)


if __name__ == '__main__':
    main()
