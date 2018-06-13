#!/usr/bin/env python
# coding=utf-8

# import local debug info module
from print_debug_info import pdi

# normal fabonacci function
def fabonacci(n):
    pdi()
    a, b = 0, 1
    for i in range(n):
        print b
        a, b = b, a + b
    pdi()

# fabonacci list generator
# 加了yield的函数就变成了生成器
def fabonacci1(n):
    pdi()
    a, b = 0, 1
    for i in range(n):
        #print b 将打印语句换成yield就能将这个函数改位生成器
        pdi()
        yield b
        pdi()
        a, b = b, a + b
    pid()

generator1 = fabonacci1(9)
# 从生成器中取数据
print(next(generator1))
print(next(generator1))
print(next(generator1))
print(next(generator1))
