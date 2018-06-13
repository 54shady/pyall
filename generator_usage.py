#!/usr/bin/env python
# coding=utf-8

# import local debug info module
from print_debug_info import pdi
from generator2 import *

# 1. 每执行一次next都会卡在yield函数
# 2. yield会返回后面的数据
# 3. 之后下次再执行next时才继续往后走
g = fabonacci(5)
print(next(g))

print('-' * 30)
print(next(g))

print('-' * 30)
print(next(g))

print('-' * 30)
print(next(g))
