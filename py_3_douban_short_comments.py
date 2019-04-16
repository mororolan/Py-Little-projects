# -*- coding:uft-8 -*-

#导入 lxml.etree 模块
from lxml import etree
#导入 用于网络访问的模块 的 requests 模块
import requests

# 讲爬虫结果存储在你想存的这个文档内
with open('./whatever_you_wanna_name.txt', 'a', encoding = 'utf-8') as f:
    for a in range(0,1000):
        #你要爬取的地址放下面
        url = 'https://movie.douban.com/subject/24852545/comments?start=' + str(a) + '&sort=new_score&status=P'
        r = requests.get(url).text
        req = etree.HTML(r)
        links = req.xpath('//*[@id="comments"]/div[1]/div[2]/p/span/text()')
        j = a + 1
        for i in links:
            f.write("%s" % j + "    :   " + i + "\n")
            j += 1
    print("_____________done_________")
    f.close()
