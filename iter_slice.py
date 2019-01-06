#!/usr/bin/env python
# coding=utf-8

from itertools import islice


def main():
    """ 使用islice对对象执行切片操作 """

    # python中的文件对象是可迭代对象
    # 假设该文件为一个大文件
    # 为了避免一次性读入过多数据到内存中
    f = open('/etc/portage/make.conf')

    # islice的第一参数是可迭代对象
    # 查看文件的第11到20行
    t = islice(f, 10, 20)
    for line in t:
        print line


if __name__ == '__main__':
    main()
