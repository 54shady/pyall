#!/usr/bin/env python
# coding=utf-8

# 限制类属性必须是slots里规定的属性
class Person(object):
    __slots__ = ("name", "age")

pObject = Person()
pObject.name = 'anonymouse'
pObject.age = 23
print '%s, age %d' % (pObject.name, pObject.age)

# 创建一个不在slots里的属性会出错
#pObject.addr = 'unknow'
