#!/usr/bin/env python
# coding=utf-8

from random import randint
from collections import Counter


def main():
    """ 统计每个数出现的次数, 并算出排名前三的数 """
    datas = [randint(0, 20) for _ in range(30)]
    print datas

    # 方法一:手工处理
    # 以datas为键,0为值创建字典
    d = dict.fromkeys(datas, 0)

    # 遍历d并统计每个数出现的次数
    for data in datas:
        d[data] += 1
    print d

    # 方法二:使用collections里Counter方法
    # 自动生成统计结果的字典
    cd = Counter(datas)
    print cd
    # 找出出现次数最多的前三个
    print cd.most_common(3)


if __name__ == '__main__':
    main()
