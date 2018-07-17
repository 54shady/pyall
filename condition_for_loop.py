#!/usr/bin/env python
# coding=utf-8


def make_a_list(condition):
    """ the condition control the for loop """
    return [x for x in range(10) if condition]


def load_file():
    with open('demofile') as f:
        lines = f.readlines()

    print 'old line0==>%s' % lines
    new_lines1 = [line for line in lines]

    # 通过if判断语句删除空行
    new_lines2 = [line for line in lines if line.strip()]

    print 'new line1==>%s' % new_lines1
    print 'new line2==>%s' % new_lines2


def main():
    list1 = make_a_list(False)
    print list1

    list2 = make_a_list(True)
    print list2

    load_file()


if __name__ == '__main__':
    main()
