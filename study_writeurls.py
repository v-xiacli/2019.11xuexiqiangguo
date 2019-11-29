import study_cookies
from selenium import webdriver
import time
import json
from bs4 import BeautifulSoup
import requests


'''
这个脚本用来获取视频链接 防止重复观看问题
'''
# def geturl_important_activities():
#     driver_video = webdriver.Chrome()
#     driver_video.get(
#         'https://www.xuexi.cn/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.html#1novbsbi47k-5')
#     driver_video.delete_all_cookies()
#     with open('cookiedata.json', 'r') as my:
#         for index in json.load(my):
#             if 'expiry' in index:
#                 del index['expiry']
#             driver_video.add_cookie(index)
#     time.sleep(1)
#     # 不要忘记refresh
#     driver_video.refresh()
#     time.sleep(8)
#
# # 预处理 先按一个 这样xpath就固定了哇 pre_clickbutton = driver_video.find_element_by_xpath('//*[
# @id="1novbsbi47k-5"]/div/div/div/div/div/div/section/div[' '3]/section/div/div/div[2]/div/div[4]') time.sleep(1)
# pre_clickbutton.click()
#
#     pre_clickbutton = driver_video.find_element_by_xpath('//*[@id="1novbsbi47k-5"]/div/div/div/div/div/div/section'
#                                                          '/div[3]/section/div/div/div[2]/div/div[6]')
#     time.sleep(1)
#     pre_clickbutton.click()
#
#     while 1:
#         data = driver_video.page_source
#         soup = BeautifulSoup(data, 'html.parser')
#         my = soup.findAll(class_="textWrapper")
#         for index in my:
#             print(index['data-link-target'])
#         clickbutton = driver_video.find_element_by_xpath('//*[@id="1novbsbi47k-5"]/div/div/div/div/div/div/section'
#                                                          '/div[3]/section/div/div/div[2]/div/div[10]')
#         time.sleep(1)
#         clickbutton.click()
#
#
# def geturl_special_report():
#     driver_specialreport = webdriver.Chrome()
#     driver_specialreport.get(
#         'https://www.xuexi.cn/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.html#1novbsbi47k-5')
#     driver_specialreport.delete_all_cookies()
#     with open('cookiedata.json', 'r') as my:
#         for index in json.load(my):
#             if 'expiry' in index:
#                 del index['expiry']
#             driver_specialreport.add_cookie(index)
#     time.sleep(1)
#     # 不要忘记refresh
#     driver_specialreport.refresh()
#     time.sleep(2)
#     pre_clickbutton = driver_specialreport.find_element_by_xpath(
#         '//*[@id="0454"]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div')
#     time.sleep(1)
#     pre_clickbutton.click()
#     time.sleep(3)
#     # 按下4
#     pre_clickbutton = driver_specialreport.find_element_by_xpath('//*[@id="1koo357ronk-5"]/div/div/div/div/div/div'
#                                                                  '/section/div[3]/section/div/div/div[2]/div/div[4]')
#     time.sleep(1)
#     pre_clickbutton.click()
#     # 按下5
#     pre_clickbutton = driver_specialreport.find_element_by_xpath('//*[@id="1koo357ronk-5"]/div/div/div/div/div/div'
#                                                                  '/section/div[3]/section/div/div/div[2]/div/div[6]')
#     time.sleep(1)
#     pre_clickbutton.click()
#
#     while 1:
#         clickbutton = driver_specialreport.find_element_by_xpath('//*[@id="1koo357ronk-5"]/div/div/div/div/div/div'
#                                                                  '/section/div[3]/section/div/div/div[2]/div/div[10]')
#         time.sleep(1)
#         clickbutton.click()
#         data = driver_specialreport.page_source
#         soup = BeautifulSoup(data, 'html.parser')
#         my = soup.findAll(class_="textWrapper")
#         for index in my:
#             print(index['data-link-target'])

'''
# 根据上面两个案例归纳出一般性解法
'''


# 利用xpath取得视频链接
def Get_Videourl_By_Xpath(xpath_targetbutton, the_4th_xpath_id):
    mydriver = webdriver.Chrome()
    mydriver.get(
        'https://www.xuexi.cn/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.html#1novbsbi47k-5')
    mydriver.delete_all_cookies()
    with open('cookiedata.json', 'r') as my:
        for index in json.load(my):
            if 'expiry' in index:
                del index['expiry']
            mydriver.add_cookie(index)
    time.sleep(1)
    # 不要忘记refresh
    mydriver.refresh()
    time.sleep(2)
    pre_clickbutton = mydriver.find_element_by_xpath(xpath_targetbutton)
    time.sleep(1)
    pre_clickbutton.click()
    time.sleep(3)
    # 按下4              1koo357ronk-5
    pre_clickbutton = mydriver.find_element_by_xpath('//*[@id="' + the_4th_xpath_id + '"]/div/div/div/div/div/div'
                                                                                      '/section/div[3]/section/div/div/div[2]/div/div[4]')

    # //*[@id="1742g60067k-5"]/div/div/div/div/div/div/section/div[3]/section/div/div/div[2]/div/div[4]

    time.sleep(1)
    pre_clickbutton.click()
    # 按下5
    pre_clickbutton = mydriver.find_element_by_xpath('//*[@id="' + the_4th_xpath_id + '"]/div/div/div/div/div/div'
                                                                                      '/section/div[3]/section/div/div/div[2]/div/div[6]')
    time.sleep(1)
    pre_clickbutton.click()

    while 1:
        clickbutton = mydriver.find_element_by_xpath('//*[@id="' + the_4th_xpath_id + '"]/div/div/div/div/div/div'
                                                                                      '/section/div[3]/section/div/div/div[2]/div/div[10]')
        time.sleep(1)
        clickbutton.click()
        data = mydriver.page_source
        soup = BeautifulSoup(data, 'html.parser')
        my = soup.findAll(class_="textWrapper")
        for index in my:
            print(index['data-link-target'])


# 利用request取得文章链接
def Get_Articalurl_By_Request(mycookies):
    cookies = '您的cookie'
    url = 'https://www.xuexi.cn/lgdata/35il6fpn0ohq.json?_st=26249200'
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/78.0.3904.97 Safari/537.36",
        'Accept': 'application/json',
        "Cookie": cookies
    }
    response = requests.get(url, headers=header)
    res = response.json()
    for index in res:
        print(index['url'])


# 获取视频专辑
Get_Videourl_By_Xpath('//*[@id="0454"]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[1]/div/div', '1novbsbi47k-5')
# 获取学习专题报道
# //*[@id="0454"]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div
Get_Videourl_By_Xpath('//*[@id="0454"]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div', "1koo357ronk-5")
# 获取学习新世界
# //*[@id="0454"]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div
Get_Videourl_By_Xpath('//*[@id="0454"]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div', "1742g60067k-5")
# 获取新闻联播
# //*[@id="0454"]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[5]/div/div
Get_Videourl_By_Xpath('//*[@id="0454"]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[5]/div/div', "17th9fq5c7l-5")


Get_Articalurl_By_Request()
