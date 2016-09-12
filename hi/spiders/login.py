#!/usr/bin/env python
# -*- coding:utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request, FormRequest


class LoginSpider(CrawlSpider):
    name = "login"
    allowed_domains = ["hi-pda.com"]
    start_urls = [
        "http://www.hi-pda.com"
    ]

    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
    "Referer": "http://www.zhihu.com/"
    }
    def start_requests(self):
        return [Request("http://www.hi-pda.com/forum/logging.php?action=login", callback = self.post_login)]  #重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数

    #FormRequeset出问题了
    def post_login(self, response):
        print 'Preparing login'
        #下面这句话用于抓取请求网页后返回网页中的formhash字段的文字, 用于成功提交表单
        formhash = response.xpath('//input[@name="formhash"]/@value').extract()[0]
        print formhash
        #FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
        #登陆成功后, 会调用after_login回调函数
        return [FormRequest.from_response(response,   #"http://www.hi-pda.com/forum/logging.php?action=login",
                            meta = {'cookiejar' : response.meta['cookiejar']}, #注意这里cookie的获取
                            headers = self.headers,
                            formdata = {
                            'formhash': xsrf,
                            'referer' : 'index.php',
                            'loginfield' : 'username',
                            'username': 'logic9034',
                            'password': '6e4015ed6197c1230bb8c34362eea93c',
                            'questionid' : '0',
                            'answer' : '',
                            'loginsubmit' : 'true',
                            'cookietime' : '2592000'
                            },
                            callback = self.after_login,
                            dont_filter = True
                            )]
    
    
    
    
    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)