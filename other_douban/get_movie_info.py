import os
import time
import sys
import random
import requests
import urllib.parse
import threading
import queue

q = queue.Queue(0)
lock = threading.RLock()

movies = []

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
    global movies
    with lock:
        if not movies:
            return
        t_movies = movies
        movies = []
        file_dir = 'movies'
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        file_name = 'movies-info-' + time.strftime('%Y-%m-%d-%H') + '.txt'
        full_file_name = os.path.join(file_dir, file_name)
        with open(full_file_name, 'a', encoding = 'utf-8') as f:
            f.write('\n'.join(t_movies) + '\n')
        t_movies = []

def save_to_error(error):
    with open('errors.txt', 'a', encoding = 'utf-8') as f:
        f.write(error + '\n') 


def get_movie_info(movie_id):
    global movies, ids
    if not is_ok():
        wait_for_ok()
    url = 'http://api.douban.com/v2/movie/subject/{}'.format(movie_id)
    remains = q.qsize()
    if remains % 100 == 0:
        print('剩余: {}'.format(remains))
    try:
        r = requests.get(url, timeout = 10)

        if r.status_code == 200:
            data = r.text
            movies.append(data)
            if len(movies) >= 10000:
                save_to_file()
        
        elif r.status_code == 403:
            print('403..............')
            q.put(movie_id)
            change_status('no')
        else:
            save_to_error(movie_id)

        
    except requests.exceptions.Timeout:
        print('timeout......')
        q.put(movie_id)

    except Exception as e:
        print(e)
        q.put(movie_id)
        change_status('no')

class MyThread(threading.Thread):
    def run(self):
        global q
        while True:
            if q.qsize() == 0:
                sys.exit()
            id = q.get()
            get_movie_info(id)

if __name__ == '__main__':
    start_time = time.time()
    t_num = 16

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
