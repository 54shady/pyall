#!/usr/bin/env python
# coding=utf-8

# import local debug info module
from print_debug_info import pdi

# fabonacci list generator
# 加了yield的函数就变成了生成器
# 1. 每执行一次next都会卡在yield函数
# 2. yield会返回后面的数据
# 3. 之后下次再执行next时才继续往后走


def fabonacci(n):
    pdi()
    a, b = 0, 1
    for i in range(n):
        # print b 将打印语句换成yield就能将这个函数改位生成器
        pdi()
        yield b
        pdi()
        a, b = b, a + b
    pdi()
