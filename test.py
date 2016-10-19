#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os,sys
import requests
import time
import os
import types 
from lxml import html
from cookielib import LWPCookieJar

COOKIE_FILE = './cookie_file'

def logLine(line):
    timeinfo = time.strftime('%Y-%m-%d %H:%M:%S -> ',time.localtime(time.time()))
    with open('logfile.txt', 'w+') as f:
        f.write(timeinfo + line)     

#os.system('sed -i 1001d %s' % filename)  删除一行

def get_ipfile():
    line = ''
    with open('iplist.txt', 'r') as f:
        line = f.readline()
        line = line.replace('\n','')
        if not line:
            return -1
    os.system('sed -i 1d iplist.txt')
    return line
        
def initLogin(proxy):
    global COOKIE_FILE
    s = requests.Session()
    s.cookies = LWPCookieJar(COOKIE_FILE)

    if not os.path.exists(COOKIE_FILE):
        # 登录并保存 cookie 到文件
        pass
    else:
        # "从 cookie 文件加载上次的 cookie，这样就不需要重复登陆"
        s.cookies.load()
        return s
    
    url = 'http://www.hi-pda.com/forum/logging.php?action=login'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8','Connection':'keep-alive','Host':'www.hi-pda.com','Upgrade-Insecure-Requests':'1'}


    try:
        r = s.get(url, headers=headers, timeout=8, proxies={'http':'http://%s' % proxy})
        r.encoding = r.apparent_encoding
        print r.apparent_encoding
        with open('testt.html', 'wb') as f:
            f.write(r.text.encode('utf-8')) 


        tree = html.fromstring(r.text)
        xsrf = tree.xpath('//input[@name="formhash"]/@value')
        if len(xsrf) < 1:
            print '403 .....'
            return -4

        payload = {                  'formhash': xsrf[0],
                                    'referer' : 'http://www.hi-pda.com/forum/logging.php?action=login',
                                    'loginfield' : 'username',
                                    'username': '',
                                    'password': 'kkkkkk',
                                    'questionid' : '0',
                                    'answer' : '',
                                    'loginsubmit' : 'true',
                                    'cookietime' : '2592000'
                                    }

        print(xsrf)

        post_url = 'http://www.hi-pda.com/forum/logging.php?action=login&loginsubmit=yes&inajax=1'
        r = s.post(post_url, data=payload, headers=headers, timeout=10, proxies={'http':'http://%s' % proxy})
        with open('testt1.html', 'wb') as f:
            f.write(r.text.encode('utf-8'))         

        #time.sleep(1)

        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8','Connection':'keep-alive','Host':'www.hi-pda.com','Upgrade-Insecure-Requests':'1','Referer':'http://www.hi-pda.com/forum/logging.php?action=login'
        }

        index_url = 'http://www.hi-pda.com/forum/index.php'
        r = s.get(index_url, headers=headers, timeout=10, proxies={'http':'http://%s' % proxy})
        r.encoding = r.apparent_encoding
        with open('testt3.html', 'wb') as f:
            f.write(r.text.encode('utf-8')) 

        if r.text.find('memcp.php') > -1:
            s.cookies.save()
            return s
    except requests.exceptions.Timeout:
        print 'timeout .....'
        return -2
    except requests.exceptions.ProxyError:
        print 'ProxyError....'
        return -3
    return -1

def saveDate(r):
        tree = html.fromstring(r.text)
        t11 = tree.xpath('//*[@id="moderate"]/table/tbody/@id')

        up_url = "http://fvgt.online/spup/addlist.php"

        for index, all_tid in enumerate(t11):
            #print index, all_tid
            #todo 0 is temp
            stid = all_tid
            tids = stid.split('_')
            #tid
            #print(tids[1])
            up_tid = tids[1].encode('utf-8')
            t22 = tree.xpath('//*[@id="thread_'+tids[1]+'"]/a')
            
            #thead
            #print t22[0].text
            #title is null
            if (type(t22[0].text) is types.NoneType):
                continue
            up_head = t22[0].text.encode('utf-8')
            
            #name
            t33 = tree.xpath('//*[@id="'+all_tid+'"]/tr/td[3]/cite/a')
            #print t33[0].text
            up_uname = t33[0].text.encode('utf-8')
            
            #ctime
            t44 = tree.xpath('//*[@id="'+all_tid+'"]/tr/td[3]/em')
            #print t44[0].text
            up_ctime = t44[0].text.encode('utf-8')
            
            #rep
            t55 = tree.xpath('//*[@id="'+all_tid+'"]/tr/td[4]/strong')
            #print t55[0].text
            up_repcnt = t55[0].text.encode('utf-8')
            
            #read
            t66 = tree.xpath('//*[@id="'+all_tid+'"]/tr/td[4]/em')
            #print t66[0].text
            up_readcnt = t66[0].text.encode('utf-8')
            
            #last time
            t77 = tree.xpath('//*[@id="'+all_tid+'"]/tr/td[5]/em/a')
            #print t77[0].text
            up_rtime = t77[0].text.encode('utf-8')

            
            payload = {
                        'tid':up_tid,
                        'head':up_head,
                        'uid':'12345',
                        'uname':up_uname,
                        'repcnt': up_repcnt,
                        'readcnt':up_readcnt,
                        'ctime':up_ctime,
                        'rtime' :up_rtime,
                        'page':page
                        
                        }

            r = requests.post(up_url, data=payload, timeout=5)

#requests.exceptions.ConnectionError
#requests.exceptions.Timeout            
def dosp(s, page, proxy):
    initpage = int(page)
    for i in range(initpage, initpage+10000):
        page = str(i)
        print "page..............:"+page

        payload = {
                    'spid':'page2',
                    'page':page
                    }

        r = requests.post("http://fvgt.online/spup/page.php", data=payload, timeout=5)
        
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8','Connection':'keep-alive','Host':'www.hi-pda.com','Upgrade-Insecure-Requests':'1','Referer':'http://www.hi-pda.com/forum/logging.php?action=login'
        }
        
        d_url = r'http://www.hi-pda.com/forum/forumdisplay.php?fid=2&page=' + page
        r = s.get(d_url, headers=headers, timeout=60, proxies={'http':'http://%s' % proxy})
        r.encoding = r.apparent_encoding
        with open('testt4.html', 'wb') as f:
            f.write(r.text.encode('utf-8')) #
            
        saveDate(r)
                




def createDaemon(page):
    # fork进程
    try:
        if os.fork() > 0: os._exit(0)
    except OSError, error:
        print 'fork #1 failed: %d (%s)' % (error.errno, error.strerror)
        os._exit(1)    
    os.chdir('/')
    os.setsid()
    os.umask(0)
    try:
        pid = os.fork()
        if pid > 0:
            print 'Daemon PID %d' % pid
            os._exit(0)
    except OSError, error:
        print 'fork #2 failed: %d (%s)' % (error.errno, error.strerror)
        os._exit(1)
    # 重定向标准IO
    sys.stdout.flush()
    sys.stderr.flush()
    si = file("/dev/null", 'r')
    so = file("/dev/null", 'a+')
    se = file("/dev/null", 'a+', 0)
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

    # 在子进程中执行代码
    dosp(page) # function demo
    
if __name__ == '__main__': 
    if (len(sys.argv)>1):
        page = sys.argv[1]
    else:
        page = '1'
    #getProxy()
    
    #获取session
    session = -1
    while session < 0:
        ip = get_ipfile()
        if (ip != -1):
            print ip
        session = initLogin(ip)
        print session
        if session < 0 :
            continue
        
        #do
        dosp(session, page, ip)
        
    #s = initLogin()
    #dosp(s, page)
    #createDaemon(page)

