#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os,sys
import requests
import time

def logLine(line):
    timeinfo = time.strftime('%Y-%m-%d %H:%M:%S -> ',time.localtime(time.time()))
    with open('logfile.txt', 'w+') as f:
        f.write(timeinfo + line)     

#os.system('sed -i 1001d %s' % filename)  删除一行
        
def getProxy():
    r = requests.get('http://api.xicidaili.com/free2016.txt', timeout=5)
    r.encoding = r.apparent_encoding
    
    ipStr = r.text
    ipList = ipStr.split('\r\n')
    print ipList

    for proxy in ipList:
        try:
            r = requests.get('http://www.qq.com/robots.txt',proxies={'http':'http://%s' % proxy}, timeout=5)
            r.encoding = r.apparent_encoding
            print r.text 
            if r.text.find('User-agent') == 0:
                print "["+proxy+"]"
                with open('iplist.txt', 'a') as f:
                    f.write(proxy + '\n')
            
        except requests.exceptions.Timeout:
            print('timeout......')
            pass
        except requests.exceptions.ProxyError:
            print('ProxyError......')
            pass
        except requests.exceptions.ConnectionError:
            print('ConnectionError......')
            pass
    

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
    getProxy() # function demo
    
if __name__ == '__main__': 
    if (len(sys.argv)>1):
        page = sys.argv[1]
    else:
        page = '1'
    while True:
        getProxy()
        time.sleep(900)
    #s = initLogin()
    #dosp(s, page)
    #createDaemon(page)

