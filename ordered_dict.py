#!/usr/bin/env python
# coding=utf-8

from time import time
from random import randint
from collections import OrderedDict


def main():
    ranks = OrderedDict()
    # 全明星技巧大赛
    # 算出用时最短的球员
    # 将结果存储在一个有序的字典中便于输出最终结果
    players = ['jordan', 'iverson', 'kobe', 'carter', 'tmac', 'garnet']
    players_nr = len(players)

    # 比赛开始时间
    start = time()

    for i in range(players_nr):
        # 假设每次输入[回车]表示一个球员完成比赛
        raw_input()
        p = players.pop(randint(0, players_nr - 1 - i))
        end = time()
        rank = i + 1
        take_times = end - start
        # 在最后加一个','表示不添加换行打印
        print rank, p, take_times,
        ranks[p] = (rank, take_times)

    # 打印一个换行
    print
    print '-' * 30
    for k in ranks:
        print k, ranks[k]


if __name__ == '__main__':
    main()
