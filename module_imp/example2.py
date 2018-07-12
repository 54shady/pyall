#!/usr/bin/env python
# coding=utf-8

import imp
import sys

class TestCls():
    module = None

    def __init__(self, **kwargs):
        # 批量初始化类属性
        for k, v in kwargs.iteritems():
          setattr(self, k, v)

        if self.module is None:
            # 通过加载模块来初始化类方法
            # 将模块中的方法变为类方法
            info = imp.find_module('say_hello', ['./localmodule/'])
            self.module = imp.load_module("hello", *info)
            print(dir(self.module))

    def _DoCall(self, function_name, *args, **kwargs):
        if self.module is None or not hasattr(self.module, function_name):
            return kwargs.get("default", None)

        return getattr(self.module, function_name)(*((self,) + args), **kwargs)

    def SayHello(self):
        return self._DoCall("sayHello")

    def SayHelloTo(self, name):
        return self._DoCall("sayHelloTo", name)

def main():
    tObj = TestCls(key1 = "value1",
                key2 = "value2",
                key3 = "value3")

    print tObj.key1
    print tObj.key2
    print tObj.key3

    #print dir(tObj)
    tObj.SayHello()
    tObj.SayHelloTo("python")

if __name__ == '__main__':
    main()
