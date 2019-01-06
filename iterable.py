#!/usr/bin/env python
# coding=utf-8


class MyRange():
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        """ 正向迭代器 """
        it = self.start
        while it <= self.end:
            yield it
            it += self.step

    def __reversed__(self):
        """ 反向迭代器 """
        it = self.end
        while it >= self.start:
            yield it
            it -= self.step


def main():
    #  列表和字符串都是可迭代对象
    l1 = [1, 2, 3]
    s1 = 'abc'

    # for循环的原理就是通过获取
    # 迭代器后执行next直到捕获到StopIteration异常后停止
    for c in l1:
        print c
    for c in s1:
        print c

    # 使用iter获取可迭代器iterator(正向迭代)
    l1_iterobj = iter(l1)
    print l1_iterobj
    s1_iterobj = iter(s1)
    print s1_iterobj

    # 需要满足可迭代的要求
    # 类内部实现__iter__可迭代接口
    # 或实现__getitem__序列接口

    # 反向迭代
    for c in reversed(l1):
        print c
    for c in reversed(s1):
        print c

    # 迭代自定义的对象
    for x in MyRange(2, 8, 2):
        print x
    print '=' * 30
    for x in reversed(MyRange(2, 8, 2)):
        print x


if __name__ == '__main__':
    main()
