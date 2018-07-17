#!/usr/bin/env python
# coding=utf-8

from Crypto.PublicKey import RSA
from Crypto import Random


INPUT_SIZE = 1024
DATA = "Hello RSA"


def main():
    random_func = Random.new().read  # 产生随机数的函数
    key_pair = RSA.generate(INPUT_SIZE, random_func)  # 生成密钥对
    private_pem = key_pair.exportKey()  # 获取pem格式的私钥
    public_pem = key_pair.publickey().exportKey()  # 获取pem格式的公钥

    public_key = RSA.importKey(public_pem)  # 输入pem格式的公钥
    encrypted = public_key.encrypt(DATA, random_func)  # 加密数据
    print encrypted

    print '-' * 30
    private_key = RSA.importKey(private_pem)  # 数据pem格式的私钥
    decrypted = private_key.decrypt(encrypted)  # 解密数据
    print decrypted


if __name__ == '__main__':
    main()
