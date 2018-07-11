#!/usr/bin/env python
# coding=utf-8

def foo():
    print 'calling foo...'
    return 0

def main():
    assert foo() == 1, 'foo should return 1 not %d' % foo()

if __name__ == '__main__':
    main()
