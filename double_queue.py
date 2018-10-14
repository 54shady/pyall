#!/usr/bin/env python
# coding=utf-8

"""
Double Queue:

add_front->  --------------------------- <-add_rear
             |   |   |    |   |   |    |
pop_front->  --------------------------- <-pop_rear
"""


class DoubleQueue():
    def __init__(self):
        """
        这里使用list(顺序表)作为底层容器
        """
        self.__queue = []

    def add_front(self, item):
        self.__queue.insert(0, item)

    def add_rear(self, item):
        self.__queue.append(item)

    def pop_front(self):
        return self.__queue.pop(0)

    def pop_rear(self):
        return self.__queue.pop()

    def is_empty(self):
        return self.__queue == []

    def size(self):
        return len(self.__queue)


def main():
    s = DoubleQueue()
    s.add_front(11)
    s.add_front(22)
    s.add_front(33)

    print 'double queue size is %d' % s.size()

    while not s.is_empty():
        print s.pop_front()

    s.add_rear(111)
    s.add_rear(222)
    s.add_rear(333)

    print 'double queue size is %d' % s.size()

    while not s.is_empty():
        print s.pop_rear()


if __name__ == '__main__':
    main()
