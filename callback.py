#!/usr/bin/env python
# coding=utf-8


def baz(age, name):
    print '%s %d' % (name, age)


def bar(name):
    print name


def foo(handler, **kwargs):
    # calling different handler
    # with different args
    if kwargs.has_key('age'):
        baz(kwargs.get('age'), kwargs.get('name'))
    else:
        bar(kwargs.get('var1'))


def main():
    foo(bar, var1="hi bar")
    foo(baz, age=23, name='hi baz')


if __name__ == '__main__':
    main()
