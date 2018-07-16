#!/usr/bin/env python
# coding=utf-8

def main():
    # version v1
    # read : read all in a str
    fd = open('/etc/fstab')

    # strip all the '\n' manually
    data = fd.read().rstrip()
    print data
    print type(data)
    fd.close()

    print '=' * 30

    # version 2
    # readlines : read all in a list
    fd = open('/etc/fstab')
    data = fd.readlines()

    # printout the data
    for i in range(len(data)):
        # strip all the '\n' manually
        print 'Line %d ==> %s' % (i, data[i].rstrip())

    print type(data)
    fd.close()

    print '=' * 30
    # version 3
    # 使用with...as可以不用手动关闭
    # 这种方式会自动关闭文件
    with open('/etc/fstab') as f:
        d = f.read().rstrip()
        print d

if __name__ == '__main__':
    main()
