#!/usr/bin/env python
# coding=utf-8

# import local debug info module
from print_debug_info import pdi

def test(number):
    pdi()

    '''在函数内部再定义一个函数,并且这个内部函数用到了外边函数的形参'''
    '''那么将这个函数及变量称作闭包'''
    '''closure就是一个闭包'''
    def closure():
        pdi()
        print(number + 99)

    pdi()
    return closure

ret = test(100)
print('='*20)
pdi()
ret()
