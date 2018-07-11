#!/usr/bin/env python
# coding=utf-8

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

if __name__ == '__main__':
    main()
