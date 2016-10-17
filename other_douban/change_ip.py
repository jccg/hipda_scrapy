import os
import time
import sys


def check_status():
    with open('status.txt', 'r', encoding = 'utf-8') as f:
        status = f.read()
        return status

def change_ip():
    time.sleep(3)
    print('Change the ip...')
    os.system("Rasdial haha /d")
    os.system("Rasdial haha 051310861177 32060200")


def change_status():
    with open('status.txt', 'w', encoding = 'utf-8') as f:
        f.write('ok')

if __name__ == '__main__':
    while True:
        try:
            if check_status() == 'no':
                change_ip()
                change_status()
            else:
                print('IP is ok')
            time.sleep(0.5)
        except KeyboardInterrupt:
            sys.exit()
