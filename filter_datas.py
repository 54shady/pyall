#!/usr/bin/env python
# coding=utf-8

from random import randint


def main():
    print 'Filter list data'
    print '=' * 30
    # generate a random list
    #sequence = [randint(-10, 10) for x in range(10)]
    sequence = [randint(-10, 10) for _ in range(10)]
    print sequence

    # 过滤掉sequence中小于3的数据

    # 方法一:使用filter
    def filter_func(x):
        return x > 3

    """
    filter函数将sequence中的每一个元素
    作为参数传给filter_func,取真值
    """
    r1 = filter(filter_func, sequence)
    print r1

    # using lambda function
    r2 = filter(lambda x: x > 3, sequence)
    print r2

    # 方法二:使用列表生成式
    r3 = [x for x in sequence if x > 3]
    print r3
    print '=' * 30

    print 'Filter dict data'
    print '=' * 30
    # ran_dict 是十个学生考试成绩
    ran_dict = {num: randint(0, 100) for num in range(10)}
    print ran_dict

    # 过滤出成绩大于80的学生的信息
    good_dict = {k: v for k, v in ran_dict.items() if v > 80}
    print good_dict
    print '=' * 30

    print 'Filter set data'
    print '=' * 30
    sequence = [randint(-100, 100) for _ in range(10)]
    print sequence
    setdata = set(sequence)
    print setdata

    # 求集合setdata中可以被3整除的数
    r = {x for x in setdata if x % 3 == 0}
    print r
    print '=' * 30


if __name__ == '__main__':
    main()
