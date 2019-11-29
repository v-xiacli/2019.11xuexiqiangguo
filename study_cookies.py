from selenium import webdriver
import time
import json

# 扫码登陆获取cookie


def lets_study_init():
    # 登陆页面
    global url_login
    url_login = "https://pc.xuexi.cn/points/login.html?ref=https%3A%2F%2Fwww.xuexi.cn%2F"


def get_study_cookies():
    lets_study_init()
    driver = webdriver.Chrome()
    driver.get(url_login)
    print("请扫码登陆")
    input("扫码完成后请按下回车键:")
    time.sleep(3)
    if driver.current_url == "https://www.xuexi.cn/":
        study_cookies = driver.get_cookies()
        driver.quit()
        return study_cookies
    else:
        driver.quit()
        return "登陆失败!"


def write_cookies_to_json(mycookie):
    # print(mycookie)
    mystr = json.dumps(mycookie)
    with open("cookiedata.json", 'a') as my:
        my.write(mystr)


def cookie_run():
    write_cookies_to_json(get_study_cookies())
