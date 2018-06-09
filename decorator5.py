#!/usr/bin/env python
# coding=utf-8

def wrapper(func):
    # 装饰带返回值的函数的装饰器
    def closure():
        r = func()
        return r

    return closure

# 带参数的装饰器
@wrapper
def function():
    return "calling function done"

# 因为装饰后function实质已经指向了闭包closure
ret = function()
print 'ret = %s' % ret
