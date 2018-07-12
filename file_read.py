#!/usr/bin/env python
# coding=utf-8

def main():
    # read : read all in a str
    fd = open('/etc/fstab')

    # strip all the '\n' manually
    data = fd.read().rstrip()
    print data
    print type(data)
    fd.close()

    print '=' * 30

    # readlines : read all in a list
    fd = open('/etc/fstab')
    data = fd.readlines()

    # printout the data
    for i in range(len(data)):
        # strip all the '\n' manually
        print 'Line %d ==> %s' % (i, data[i].rstrip())

    print type(data)
    fd.close()

if __name__ == '__main__':
    main()
