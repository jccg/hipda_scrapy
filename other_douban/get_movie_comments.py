import os
import time
import sys
import random
import requests
import urllib.parse
import threading
import queue
import re

q = queue.Queue(0)
lock = threading.RLock()

comments = []

def is_ok():
    with open('status.txt', 'r', encoding = 'utf-8') as f:
        status = f.read()
        if status == 'ok':
            return True
        else:
            return False

def wait_for_ok():
    while True:
        print('Waiting for status be ok')
        if is_ok():
            return
        time.sleep(2)

def change_status(status):
    with open('status.txt', 'r+', encoding = 'utf-8') as f:
        f.seek(0)
        f.truncate()
        f.write(status)

def save_to_file():
    global comments
    with lock:
        if not comments:
            return
        t_comments = comments
        comments = []
        file_dir = 'movies'
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        file_name = 'movie-comments-' + time.strftime('%Y-%m-%d-%H') + '.txt'
        full_file_name = os.path.join(file_dir, file_name)
        with open(full_file_name, 'a', encoding = 'utf-8') as f:
            f.write('\n'.join(t_comments) + '\n')
        t_comments = []

def save_to_error(error):
    with open('errors.txt', 'a', encoding = 'utf-8') as f:
        f.write(str(error) + '\n') 


def get_movie_comments(movie_id):
    global comments, ids
    
    remains = q.qsize()
    if remains % 10 == 0:
        print('剩余: {}'.format(remains))
    start = 0
    c_comments = set()
    pattern_comment = re.compile('<p class=\"\">(.*?)</p>')
    pattern_html_tag = re.compile('<.*?>')
    while True:
        if len(c_comments) > 100:
            break
        if not is_ok():
            wait_for_ok()
        
        url = 'https://movie.douban.com/subject/{}/comments?start={}&limit=20&sort=new_score'.format(movie_id, start)
        try:
            r = requests.get(url, timeout = 10, allow_redirects = False)
            data = r.text.replace('\r', '').replace('\n', '')
            if r.status_code == 200:
                start = start + 20
                lines = pattern_comment.findall(data)
                if len(lines) == 0:
                    # print('后面没有了...............')
                    break
                for line in lines:
                    line = line.strip()
                    line = pattern_html_tag.sub('', line)
                    c_comments.add(str(movie_id) + '|====|' + line)
				if len(c_comments) > 100:
					# print('已经抓取到100条了...............')
					break

            elif r.status_code == 302:
                # print('302.................')
                break
            elif r.status_code == 404:
                # print('404.................')
                break
            elif r.status_code == 403:
                if '403 Forbidden' in data:
                    # print('403..............')
                    change_status('no')
                elif '没有访问权限' in data:
                    # print('后面没有了......')
                    break
            else:
                # print('error............')
                save_to_error(url)
                break
        except requests.exceptions.Timeout:
            # print('timeout......')
            pass
        except Exception as e:
            print(e)
            break

    c_comments = list(c_comments)[:100]
    comments.extend(c_comments)
    if len(comments) > 1000:
        save_to_file()

class MyThread(threading.Thread):
    def run(self):
        global q
        while True:
            if q.qsize() == 0:
                sys.exit()
            id = q.get()
            get_movie_comments(id)

if __name__ == '__main__':
    start_time = time.time()
    t_num = 8

    with open('movie_ids.txt','r', encoding = 'utf-8') as f:
        ids = f.readlines()
        ids = [id.strip() for id in ids]
        for id in ids:
            q.put(id)
        
    threads = []
    for i in range(t_num):
        t = MyThread()
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    save_to_file()
    print((time.time() - start_time) / 60)

    # get_movie_comments(4811813)

