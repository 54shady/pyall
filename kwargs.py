#!/usr/bin/env python
# coding=utf-8

class TestCls():
    def foo(self, name, *args, **kwargs):
        print name
        # 获取字典中key为default的值,如果没有该key则值为第二个参数(None)
        print kwargs.get('default', None)

def main():
    tObj = TestCls()
    tObj.foo("testDemo")

if __name__ == '__main__':
    main()
