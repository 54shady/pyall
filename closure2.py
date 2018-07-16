#!/usr/bin/env python
# coding=utf-8

# 闭包的应用

# 描述y = ax + b这个函数(直线)


def line_config(a, b):
    def line(x):
        return a * x + b

    return line


# 两条直线
line1 = line_config(1, 1)
line2 = line_config(2, 5)

# 给出x值求y的值
y1 = line1(5)
print(y1)

y2 = line2(5)
print(y2)
