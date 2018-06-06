#!/usr/bin/env python
# coding=utf-8

# value1 can be access by 'from private import *'
value1=100

# _value2 can not be access by 'from private import *'
_value2=200

class Person():
    def __init__(self):
        self.__age = 9
        self.__name = 'anonymous'

    def get_age(self):
        print '%s age is %s' % (self.__name, self.__age)

    def set_age(self, n):
        print 'set %s age to %s' % (self.__name, n)
        self.__age = n

p = Person()

# dir(p)
# 可以看到私有的属性被改名了
# _Person__age, _Person__name
# print dir(p)

p.get_age()
p.set_age(911)
p.get_age()
