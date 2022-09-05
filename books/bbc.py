#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return BBCChinese

class BBCChinese(BaseFeedBook):
    title                 = u'BBC中文网'
    description           = u'英国广播公司中文网站。'
    language              = 'zh-Hans'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_bbc.gif"
    coverfile             = "cv_bbc.jpg"
    oldest_article        = 1
    
    feeds = [
            (u'BBC Chinese', 'http://www.bbc.co.uk/zhongwen/simp/index.xml'),
            ]
    
    def fetcharticle(self, url, opener, decoder):
        #每个URL都增加一个后缀full=y，如果有分页则自动获取全部分页
        url += '?full=y'
        return BaseFeedBook.fetcharticle(self,url,opener,decoder)
        
