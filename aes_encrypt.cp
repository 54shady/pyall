#!/usr/bin/env python
# coding=utf-8

from Crypto.Cipher import AES


# 加密和解密用的通用密钥(加解密同一个密钥)
# 密钥可以是长度为16、24、32 字符的任意字符串
KEY = "this_key_for_encrypt_and_decrypt"

# 要加密的数据,长度为16的倍数
DATA = "0123456789abcdef"


def main():
    assert len(KEY) in (16, 24, 32)  # 确保密钥长度正确
    aes = AES.new(KEY)  # 生产AES类的实例
    encrypt_data = aes.encrypt(DATA)  # 加密数据
    print repr(encrypt_data)
    decrypt_data = aes.decrypt(encrypt_data)  # 解密数据
    print repr(decrypt_data)


if __name__ == '__main__':
    main()
