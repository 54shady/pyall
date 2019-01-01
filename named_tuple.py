#!/usr/bin/env python
# coding=utf-8

from collections import namedtuple

# 类似C语言的枚举类型
NAME, AGE, SEX, MAIL = range(4)


def main():
    # 方法一:使用类似C语言中的枚举类型
    player1 = ('Eminem', 28, 'male', 'shady@aftermath.com')
    print player1
    # 这样就可以使用下标来方便访问
    print player1[NAME]
    print player1[MAIL]

    # 方法二:使用库collections里的namedtuple
    Player = namedtuple('Player', ['NAME', 'AGE', 'SEX', 'MAIL'])
    player2 = Player('Shady', 21, 'female', 'eminem@slime.com')
    print player2
    # 使用下标访问
    print player2[NAME]
    print player2[MAIL]
    # 还可以使用访问类属性的方法
    print player2.AGE
    print player2.SEX

    # 创建的player2是一个tuple的子类
    print isinstance(player2, tuple)


if __name__ == '__main__':
    main()
