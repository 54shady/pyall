#!/usr/bin/env python
# coding=utf-8


def wrapper(func):
    def closure(a, b):
        return 911 + func(a, b)

    return closure


@wrapper
def function(x, y):
    # 带参数的装饰器
    return x + y


# 因为装饰后function实质已经指向了闭包closure
# 所以要装饰带参数的函数,闭包函数要和被装饰的参数有相同的形参
ret = function(1, 2)
print 'ret = %d' % ret
