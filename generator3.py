#!/usr/bin/env python
# coding=utf-8

# import local debug info module
from print_debug_info import pdi
from generator2 import *

# 生成器在for循环中的使用方法, 不需要使用next
generator1 = (x + 2 for x in range(10))
for i in generator1:
    print i

# 1. 每执行一次next都会卡在yield函数
# 2. yield会返回后面的数据
# 3. 之后下次再执行next时才继续往后走
g = fabonacci(5)
# print(type(g)) g是生成器对象
# next(g) 或者 g.__next__()

# help(next)
# 使用for循环来调用生成器
for n in g:
    # print(type(n)) 这里的n是个int不是generator
    print(n) # 不是next(n), next(iterator)
