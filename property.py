#!/usr/bin/env python
# coding=utf-8

class Person():
    def __init__(self):
        self.__age = 9

    def get_age(self):
        return self.__age

    def set_age(self, n):
        self.__age = n

    interface_age = property(get_age, set_age)

p = Person()
print 'age is %d' % (p.interface_age)
p.interface_age = 100
print 'age is %d' % (p.interface_age)
