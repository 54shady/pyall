#!/usr/bin/env python
# coding=utf-8

import socket


def get_host_ip():
    '''
    利用UDP协议来实现的,生成一个UDP包,
    把自己的IP放到UDP协议头中,然后从UDP包中获取本机的IP.
    这个方法并不会真实的向外部发包,所以用抓包工具是看不到的.
    但是会申请一个UDP的端口,所以如果经常调用也会比较耗时的,
    这里如果需要可以将查询到的IP给缓存起来,性能可以获得很大提升
    '''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def main():
    local_ip = get_host_ip()
    print local_ip


if __name__ == '__main__':
    main()
