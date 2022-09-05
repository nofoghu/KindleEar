#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return BBCChinese

class BBCChinese(BaseFeedBook):
    title                 = u'BBC中文网'
    description           = u'英国广播公司中文网站。'
    language              = 'zh-Hans'
    feed_encoding         = "zh-Hans"
    page_encoding         = "zh-Hans"
    mastheadfile          = "mh_bbc.gif"
    coverfile             = "cv_bbc.jpg"
    oldest_article        = 1
    
    feeds = [
            (u'BBC Chinese', 'https://feeds.bbci.co.uk/zhongwen/simp/rss.xml'),
            ]
    
    def fetcharticle(self, url, opener, decoder):
        #每个URL都增加一个后缀full=y，如果有分页则自动获取全部分页
        url += '?full=y'
        return BaseFeedBook.fetcharticle(self,url,opener,decoder)
        
