#!/usr/bin/env python
# coding=utf-8


class Queue():
    def __init__(self):
        """
        这里使用list(顺序表)作为底层容器
        """
        self.__queue = []

    def enqueue(self, item):
        """ 尾部入列 """
        self.__queue.append(item)

    def dequeue(self):
        """ 头部出列 """
        return self.__queue.pop(0)

    def is_empty(self):
        """
        判断栈是否为空
        return self.__queue也能达到效果
        但是这样违背了将内部数据私有化的原则
        将内部私有化数据返回给外部

        return self.__queue == []
        """
        return len(self.__queue) == 0

    def size(self):
        """ 返回栈的元素的个数 """
        return len(self.__queue)


def main():
    s = Queue()
    s.enqueue(11)
    s.enqueue(22)
    s.enqueue(33)

    print 'queue size is %d' % s.size()

    while not s.is_empty():
        print s.dequeue()


if __name__ == '__main__':
    main()
