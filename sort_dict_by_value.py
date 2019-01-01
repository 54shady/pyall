#!/usr/bin/env python
# coding=utf-8


from random import randint


def main():
    """ 将字典按照值排序 """

    d = {x: randint(0, 100) for x in 'abcdef'}
    print d

    # 方法一:先使用zip转化成list,再用sorted排序
    # 将字典的键和值对调生成新的字典
    #dd = zip(d.values(), d.keys())
    # 使用iter的版本会减少存储空间
    dd = zip(d.itervalues(), d.iterkeys())
    print dd
    # 巧妙使用sorted排序,达到按照值排序的结果
    print sorted(dd)

    # 方法二:使用sorted中自定义key排序
    # sorted的参数key用来指定用按这个key排序
    # lambda中x表示d.items()中的每一个键值对
    # x[1]表示取的是值
    # key=字典中的值,所以sorted是按找值来排序
    res = sorted(d.items(), key=lambda x: x[1])
    print res


if __name__ == '__main__':
    main()
