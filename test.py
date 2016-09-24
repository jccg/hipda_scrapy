#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import requests
import time
from lxml import html

s = requests.Session()


url = 'http://www.hi-pda.com/forum/logging.php?action=login'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8','Connection':'keep-alive','Host':'www.hi-pda.com','Upgrade-Insecure-Requests':'1'}



r = s.get(url, headers=headers)
r.encoding = r.apparent_encoding
print r.apparent_encoding
with open('testt.html', 'wb') as f:
    f.write(r.text.encode('utf-8')) 


tree = html.fromstring(r.text)
xsrf = tree.xpath('//input[@name="formhash"]/@value')[0]

payload = {                  'formhash': xsrf,
                            'referer' : 'http://www.hi-pda.com/forum/logging.php?action=login',
                            'loginfield' : 'username',
                            'username': 'logic90',
                            'password': 'xxxxxxxxxxxxxxxxxxxxxxx',
                            'questionid' : '0',
                            'answer' : '',
                            'loginsubmit' : 'true',
                            'cookietime' : '2592000'
                            }

print(xsrf)

post_url = 'http://www.hi-pda.com/forum/logging.php?action=login&loginsubmit=yes&inajax=1'
r = s.post(post_url, data=payload, headers=headers)
with open('testt1.html', 'wb') as f:
    f.write(r.text.encode('utf-8'))         

#time.sleep(1)

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8','Connection':'keep-alive','Host':'www.hi-pda.com','Upgrade-Insecure-Requests':'1','Referer':'http://www.hi-pda.com/forum/logging.php?action=login'
}

index_url = 'http://www.hi-pda.com/forum/index.php'
r = s.get(index_url, headers=headers)
r.encoding = r.apparent_encoding
with open('testt3.html', 'wb') as f:
    f.write(r.text.encode('utf-8')) 
    
d_url = 'http://www.hi-pda.com/forum/forumdisplay.php?fid=2'
r = s.get(d_url, headers=headers)
r.encoding = r.apparent_encoding
with open('testt4.html', 'wb') as f:
    f.write(r.text.encode('utf-8')) #
    

tree = html.fromstring(r.text)
t11 = tree.xpath('//*[@id="moderate"]/table/tbody/@id')

with open('result.txt', 'ab') as f:
    #f.write(r.text.encode('utf-8')) #
    for index, all_tid in enumerate(t11):
        print index, all_tid
        #todo 0 is temp
        s = all_tid
        tids = s.split('_')
        #tid
        #print(tids[1])
        f.write(tids[1].encode('utf-8')) #
        t22 = tree.xpath('//*[@id="thread_'+tids[1]+'"]/a')
        #thead
        #print t22[0].text
        f.write(t22[0].text.encode('utf-8')) #
        #name
        t33 = tree.xpath('//*[@id="'+all_tid+'"]/tr/td[3]/cite/a')
        #print t33[0].text
        f.write(t33[0].text.encode('utf-8')) #
        #ctime
        t44 = tree.xpath('//*[@id="'+all_tid+'"]/tr/td[3]/em')
        #print t44[0].text
        f.write(t44[0].text.encode('utf-8')) #
        #rep
        t55 = tree.xpath('//*[@id="'+all_tid+'"]/tr/td[4]/strong')
        #print t55[0].text
        f.write(t55[0].text.encode('utf-8')) #
        #read
        t66 = tree.xpath('//*[@id="'+all_tid+'"]/tr/td[4]/em')
        #print t66[0].text
        f.write(t66[0].text.encode('utf-8')) #
        #last time
        t77 = tree.xpath('//*[@id="'+all_tid+'"]/tr/td[5]/em/a')
        #print t77[0].text
        f.write(t77[0].text.encode('utf-8')) #


