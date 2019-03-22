#!/usr/bin/env python
# coding=utf-8

import json
import os
import shutil


def ncopy(src_file_or_dir, dst_dir, target_name=None):
    """
    A powerfull copy function

    @src_file_or_dir can be a dir or a file
    @dst_dir the destination directory

    cp a_dir to dst_dir/a_dir
    cp a_file to dst_dir/a_file

    @target_name
    leave the target_name empty
    if u don't wanna change the file name
    """

    # find out the absolute path of src_file_or_dir and dst
    abs_src = os.path.abspath(src_file_or_dir)
    abs_dst_dir = os.path.abspath(dst_dir)
    if not os.path.exists(abs_dst_dir):
        shutil.os.makedirs(abs_dst_dir)

    # rename the file or keey the origin file name
    # split src_file_or_dir file path and file name
    fp, fn = os.path.split(abs_src)
    if target_name is None:
        dst_file_name = fn
    else:
        dst_file_name = target_name

    # the absolute destination file path
    abs_dst = os.path.join(abs_dst_dir, dst_file_name)

    if (os.path.isdir(abs_src)):
        if os.path.exists(abs_dst):
            shutil.rmtree(abs_dst)
            shutil.copytree(abs_src, abs_dst)
        else:
            shutil.copytree(abs_src, abs_dst)
    elif (os.path.isfile(abs_src)):
        shutil.copy2(abs_src, abs_dst)
    else:  # links, pipes, chars, etc
        shutil.copy2(abs_src, abs_dst)


def main():
    """
    1       alias aaa
    ├── danmaku.xml
    ├── entry.json  alias entry_json
    └── lua.flv360.bili2api.16
        ├── 0.blv alas target_blv
            ├── 0.blv.4m.sum
                └── index.json
    """

    aaas = os.listdir(os.getcwd())

    for aaa in aaas:
        if (os.path.isdir(aaa)):
            #print 'dir : %s ' % aaa
            entry_json = os.path.join(aaa, "entry.json")
            try:
                with open(entry_json, "r") as f:
                    json_str = json.load(f)
            except IOError:
                print 'No such file'
                continue

            target_blv = os.path.join(aaa, json_str['type_tag'], "0.blv")
            target_dir = os.getcwd() + '/' + json_str['title']
            if not os.path.exists(json_str['title']):
                os.mkdir(target_dir)

            if os.path.exists(entry_json) and os.path.exists(target_blv):
                new_blv_name = json_str['page_data']['part'] + ".blv"
                # delete the space in the middle of the str
                new_blv_name = "".join(new_blv_name.split())
                print '%s title is %s' % (
                    os.path.relpath(entry_json), new_blv_name)
                ncopy(target_blv, target_dir, new_blv_name)


if __name__ == '__main__':
    main()
