#!/usr/bin/env python
# coding=utf-8

import urllib
import urllib2

# using baidu to search keyword

# url prefix
tmp_url = "http://www.baidu.com/s"

# enter the keyword for searching
keyword = raw_input("Enter the keyword: ")

# encode the keyword for url
query = {'wd': keyword}
kw = urllib.urlencode(query)

# baidu search url format
url = tmp_url + "?" + kw

# headers for the reqest
headers = {"User-Angent": "Mozilla 5.10"}

# url request and open
request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)

# read from response
html = response.read()
print html

# save the result
filename = keyword + ".html"
with open(filename, "w") as fn:
    fn.write(html)
