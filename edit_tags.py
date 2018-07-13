#!/usr/bin/env python
# coding=utf-8

# 根据第一个字符是+/-来决定是否保留或添加tag
tags_changes = ('-/xxoo/tags', '+/this/tags')

def EditTags(tags):
    """Given a string containing comma-separated tags, apply the edits
  specified in tag_changes and return the updated string."""

    # set的元素没有重复,而且是无序的
    # 使用set()将重复的元素删除
    tags = set(tags.split(","))

    for ch in tags_changes:
        if ch[0] == "-":
            tags.discard(ch[1:])
            #print 'remove %s' % ch[1:]
        elif ch[0] == "+":
            tags.add(ch[1:])
            #print 'add %s' % ch[1:]

    return ",".join(sorted(tags))

def main():
    oldtags = (
            "/home/tags,"
            "/home/tags,"
            "/xxoo/tags,"
            "/opt/tags,"
            "/path/abcd/tags,"
            )
    print 'old tags ==> %s' % oldtags
    newtags = EditTags(oldtags)
    print 'new tags ==> %s' % newtags

if __name__ == '__main__':
    main()
