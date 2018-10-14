#!/usr/bin/env python
# coding=utf-8


class Stack():
    def __init__(self):
        """
        这里使用list(顺序表)作为底层容器
        """
        self.__stack = []

    def push(self, item):
        """
        1. 这里不使用list的insert操作
            self.__stack.insert(item)
            因为对于顺序表尾部操作复杂度是O(1)
            而对于头部操作复杂度是O(N)
        2. 如果使用的底层容器类型是链表
            则应该在头部插入新数据和取数据
        """
        self.__stack.append(item)

    def pop(self):
        """
        如果在push的时候是用insert的话
        pop的就需要pop(0)
        但是这样同样是操作顺序表的头
        """
        return self.__stack.pop()

    def peek(self):
        """ 返回栈顶元素 """
        if self.__stack:
            return self.__stack[-1]
        else:
            return None

    def is_empty(self):
        """
        判断栈是否为空
        return self.__stack也能达到效果
        但是这样违背了将内部数据私有化的原则
        将内部私有化数据返回给外部

        return self.__stack == []
        """
        return len(self.__stack) == 0

    def size(self):
        """ 返回栈的元素的个数 """
        return len(self.__stack)


def main():
    s = Stack()
    print s.peek()
    s.push(11)
    s.push(22)
    s.push(33)

    print 'stack size is %d' % s.size()
    print 'stack peek item is %d' % s.peek()

    while not s.is_empty():
        print s.pop()


if __name__ == '__main__':
    main()
