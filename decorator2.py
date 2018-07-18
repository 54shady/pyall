#!/usr/bin/env python
# coding=utf-8

""" 装饰器装饰的时机 """

import time


def makeBold(fn):
    print("wrapping....")

    def wrapper():
        fn()

    return wrapper


@makeBold
def function():
    print("calling function")


# 即使还没调用函数function但是python解析器已经装饰好了
time.sleep(3)
function()
