#!/usr/bin/env python
# coding=utf-8

def main():
    print 'raw input>'
    # input will always be string type
    # 随便输都是字符串
    s1 = raw_input()
    print type(s1)

    print 'input>'
    # 必须按照Python的规则格式输入
    # input should in format
    # int : 123
    # str : 'string' "string"
    s2 = input()
    print type(s2)

if __name__ == '__main__':
    main()
