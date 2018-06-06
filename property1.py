#!/usr/bin/env python
# coding=utf-8

class Person():
    def __init__(self):
        self.__age = 9

    # get 方法用property装饰器装饰
    # 之后就有一个person_age的装饰器
    @property
    def person_age(self):
        print('get age')
        return self.__age

    # set方法直接在装饰器名后加setter
    @person_age.setter
    def person_age(self, n):
        print('set age')
        self.__age = n

p = Person()

# 使用的时候就是直接调用装饰器的名字
print 'age is %d' % (p.person_age)
p.person_age = 100
print 'age is %d' % (p.person_age)
