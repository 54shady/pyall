#!/usr/bin/env python
# coding=utf-8


import urllib
import urllib2


def loadPage(url, filename):
    """
        作用：根据url发送请求，获取服务器响应文件
        url: 需要爬取的url地址
        filename : 处理的文件名
    """
    print "Download >>> " + filename
    headers = {"User-Agent": "Mozilla/5.0"}
    request = urllib2.Request(url, headers=headers)
    return urllib2.urlopen(request).read()


def writePage(html, filename):
    """
        作用：将html内容写入到本地
        html：服务器相应文件内容
    """
    print "Saving >>> " + filename
    with open(filename, "w") as fn:
        fn.write(html)


def tiebaSpider(url, beginPage, endPage):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url : 贴吧url的前部分
        beginPage : 起始页
        endPage : 结束页
    """
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        filename = "Page" + str(page) + ".html"
        target_url = url + "&pn=" + str(pn)
        # print target_url
        html = loadPage(target_url, filename)
        # print html
        writePage(html, filename)


if __name__ == '__main__':
    # baidu tieba spider
    keyword = raw_input("Enter the tieba name: ")
    beginPage = int(raw_input("Enter the first page: "))
    endPage = int(raw_input("Enter the last page: "))

    tmp_url = "http://tieba.baidu.com/f?"
    query = {"kw": keyword}
    kw = urllib.urlencode(query)
    url = tmp_url + kw
    tiebaSpider(url, beginPage, endPage)
