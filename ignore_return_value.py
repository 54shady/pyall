#!/usr/bin/env python
# coding=utf-8

temp_list = [(1, 2), (3, 4), (5, 6)]

# 函数放回多个返回值


def foo():
    return 1, 2


def main():
    a, b = foo()
    print a, b

    r = foo()
    print r

    (x, y) = foo()
    print x, y

    # 在接受返回值的时候可以忽略不关注的返回值
    # 用_替代
    (_, n) = foo()
    print n

    (i, _) = foo()
    print i

    print '-' * 30
    for (x, y) in temp_list:
        print x, y

    # 同理在遍历的时候也可以用_来达到同样效果
    print '-' * 30
    for (_, y) in temp_list:
        print y

    print '-' * 30
    for (x, _) in temp_list:
        print x


if __name__ == '__main__':
    main()
