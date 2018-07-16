#!/usr/bin/env python
# coding=utf-8


class ExternalError(RuntimeError):
    pass


def main():
    v = input()
    if v != 1:
        raise ExternalError('input value %d error(must be 1)' % v)


if __name__ == '__main__':
    main()
