#!/usr/bin/env python
# coding=utf-8

# import local debug info module
from print_debug_info import pdi


def test():
    i = 0
    while i < 10:
        # 这里给temp赋值
        # 当使用send后,传入的参数会替换给temp赋值语句中等号右边的所有部分
        temp = yield i
        print 'temp value = %s' % temp
        # print(type(temp))
        i += 1


tObject = test()

# 不能一开始就使用send
# tObject.send('firsttime')
# 所以第一次使用的时候必须调用next或使用send(None)
tObject.send(None)

print('-' * 35)
print(tObject.next())
print(tObject.next())

print('-' * 35)
# 当使用send后,先将send传入的参数替换给temp赋值语句中等号右边的所有部分
tObject.send('debuginfo')
tObject.send(123)

print('-' * 35)
# 再次调用是temp又为空
print(tObject.next())
