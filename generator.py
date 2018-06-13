#!/usr/bin/env python
# coding=utf-8

# 列表生成式
list1 = [x*2 for x in range(10)]
print list1

# 使用生成器的目的是为了节省内存资源
# 在使用到数据的时候才取临时生成数据
# 将列表生成式的方括号改为园括号
generator1 = (x*2 for x in range(10))
print generator1

# 使用next来获取生成器的值
print next(generator1)
print next(generator1)
print next(generator1)
print next(generator1)
