import study_cookies
from selenium import webdriver
import time
import os
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
from bs4 import BeautifulSoup
import re

# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument('--headless')


if not os.path.exists('cookiedata.json'):
    study_cookies.cookie_run()


def study_data_init():
    # 新闻链接页面
    global mynews
    mynews = 'https://www.xuexi.cn/98d5ae483720f701144e4dabf99a4a34/5957f69bffab66811b99940516ec8784.html'
    global myvideo
    myvideo = 'https://www.xuexi.cn/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.html' \
              '#1novbsbi47k-5 '


def get_data(filepath):
    my = open(filepath)
    urls = my.read().splitlines()
    return urls


def save_data(filepath, data):
    with open(filepath, 'w') as f:
        for index in data:
            f.write(index + '\n')


def study_read_news():
    allarticals = get_data('artical_urls.txt')
    artical_haveread = get_data('artical_haveread.txt')
    # 开始登陆
    browser_artical = webdriver.Chrome()
    browser_artical.get(myvideo)
    browser_artical.delete_all_cookies()
    with open('cookiedata.json', 'r') as my:
        for index in json.load(my):
            if 'expiry' in index:
                del index['expiry']
            browser_artical.add_cookie(index)
    time.sleep(2)
    # 不要忘记refresh
    browser_artical.refresh()
    cnt = 1
    # 模拟人类滚动
    for index in allarticals:
        if index not in artical_haveread:
            browser_artical.get(index)
            artical_haveread.append(index)
            print('condition: ' + str(cnt) + '/' + '7')
            time.sleep(1)
            # 取随机值
            for i in range(random.randint(4000, 5000)):
                browser_artical.execute_script('window.scrollTo(0, ' + str(i) + ')')
            time.sleep(random.randint(120, 150))
            # 超过7个文章
            if cnt >= 7:
                break
            cnt += 1
    save_data('artical_haveread.txt', artical_haveread)
    print("看文章结束！")
    browser_artical.quit()


def study_watch_video():
    # 所有视频地址的列表
    allvideos = get_data('video_urls.txt')
    # 我已经看的内容
    ihaveread = get_data('video_haveread.txt')
    # 开始登陆
    # print(allvideos)
    # print(ihaveread)
    browser_video = webdriver.Chrome()
    wait = WebDriverWait(browser_video, 10)
    browser_video.get(myvideo)
    browser_video.delete_all_cookies()
    with open('cookiedata.json', 'r') as my:
        for index in json.load(my):
            if 'expiry' in index:
                del index['expiry']
            browser_video.add_cookie(index)
    time.sleep(2)
    # 不要忘记refresh
    browser_video.refresh()
    cnt = 1
    for index in allvideos:
        if index not in ihaveread:
            ihaveread.append(index)
            print('condition: ' + str(cnt) + '/' + '7')
            browser_video.get(index)
            data = browser_video.page_source
            soup = BeautifulSoup(data, 'html.parser')
            mydata = soup.find_all(class_='duration')
            # 获取片的总时长 加上30秒缓冲时间
            print(mydata)
            mytime = int(str(mydata[0])[49]) * 60 + 30
            print('该片需要看的时间为:' + str(mytime))
            try:
                button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'prism-big-play-btn')))
                button.click()
            finally:
                time.sleep(mytime)
                # 超过7个片
                if cnt >= 7:
                    break
                cnt += 1
    save_data('video_haveread.txt', ihaveread)
    print("看片结束！")
    browser_video.quit()


study_data_init()
# study_read_news()
study_watch_video()
