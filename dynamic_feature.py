#!/usr/bin/env python
# coding=utf-8

import types

class Person(object):
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

    def eat(self):
        print '%s is eatting' % self.name

pObject = Person("anonymouse", 100)
print(pObject.name)
print(pObject.age)

# 给当前类对象动态添加属性
pObject.addr = "Unkonw"
print(pObject.addr)

# 给所有类对象都添加属性
Person.number = 911
print(pObject.number)

pObject.eat()

print('-' * 30)
# 给当前对象动态添加方法
def newRun(obj):
    print '%s is running' % obj.name

#pObject.run = newRun
#pObject.run(pObject)

# 给实例添加方法
# 使用MethodType来动态给类对象添加方法
# 将newRun的第一个参数绑定为pObject
pObject.run = types.MethodType(newRun, pObject)
pObject.run() # 这样调用该函数时,就能自动将类当作参数传进去

print('-' * 30)
ret = types.MethodType(newRun, pObject)
ret()

# 给类添加方法
# 静态方法
@staticmethod
def fly():
    print 'static method, flying'

Person.fly = fly
pObject.fly()

# 类方法
@classmethod
def read(cls):
    print 'reading...'

Person.read = read
pObject.read()
