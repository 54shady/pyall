#!/usr/bin/env python
# coding=utf-8


class MyFileClass(object):
    """
    调用类方法实现打开一个文件
    并将文件内容保存,且记录文件相应名字
    """

    def __init__(self, name, data):
        self.name = name
        self.data = data

    @classmethod
    def load_file(cls, nickname, filename):
        '''
        nickname : is an alias name for the filename
        filename : is the real name on the disk
        example :
            filename maybe "/path/to/the/realfile.txt"
            nickname maybe "realfile"
        '''
        with open(filename) as f:
            data = f.read()
            return MyFileClass(nickname, data)


def main():
    obj = MyFileClass.load_file('partitionfile', '/etc/fstab')
    print obj.name
    print obj.data


if __name__ == '__main__':
    main()
