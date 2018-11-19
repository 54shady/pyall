#!/usr/bin/env python
# coding=utf-8

'''
====== Link List Test ======
[m]enu show
[i]nsert node
[s]how list
[x]delete node
[l]ist len
[q]uit
=============================
'''

import sys


class SingleListNode():
    def __init__(self, data, next_node=None):
        self.next = next_node
        self.data = data

    def __str__(self):
        return self.data


class SingleList():
    def __init__(self, head=None):
        self.head = head
        self.len = 0

    def list_len(self):
        return self.len

    def insert_node_front(self, data):
        node = SingleListNode(data)
        node.next = self.head
        self.head = node
        self.len += 1

    def traverse(self, handler, **kwargs):
        iterator = self.head
        # if we got key, which means need search
        has_key = kwargs.has_key('key')
        while iterator:
            # search node case
            if has_key:
                ret = handler(iterator, kwargs.get('key'))
                if ret:
                    return ret
                else:
                    pass
            # normal case
            else:
                handler(iterator)
            iterator = iterator.next
        return None

    def print_data(self, node):
        print node.data,

    def show_datas(self):
        self.traverse(self.print_data)
        print '\n'

    def compare_node(self, node, key):
        # compare node data
        if node.data == key:
            return node
        return None

    def search_node(self, key):
        """ search key node """
        return self.traverse(self.compare_node, key=key)

    def delete_node(self, this):
        # delete this node
        if not self.head:
            print 'empyt list'
            return

        # delete head node
        if self.head.data == this.data:
            self.head = self.head.next
            self.len -= 1
            return

        prev_node = self.head
        cur_node = self.head.next
        while cur_node:
            if cur_node.data == this.data:
                prev_node.next = cur_node.next
                self.len -= 1
                return
            prev_node = cur_node
            cur_node = cur_node.next


def main():
    single_list = SingleList()

    print __doc__
    while True:
        print 'Enter cmd:',
        cmd = raw_input()
        if 'm' == cmd:
            print __doc__
        elif 'i' == cmd:
            print 'insert node'
            print 'Enter node data:',
            node_data = input()
            print node_data
            single_list.insert_node_front(node_data)
        elif 's' == cmd:
            single_list.show_datas()
        elif 'x' == cmd:
            print 'Enter delete node data:',
            delete_node_data = input()
            print delete_node_data
            node = single_list.search_node(delete_node_data)
            if isinstance(node, SingleListNode):
                single_list.delete_node(node)
            else:
                print 'Node %d not found' % delete_node_data
        elif 'l' == cmd:
            print 'len = %d' % single_list.len
        elif 'q' == cmd:
            sys.exit(0)
        else:
            print __doc__


if __name__ == '__main__':
    main()
