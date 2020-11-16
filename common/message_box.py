# -*- coding: utf-8 -*-
# @Time    : 2020/10/19 11:03
# @Author  : Wang Bingyin
# @Email   : xxxxxxx@163.com
# @File    : message_box.py
# @Software: PyCharm
import time
from selenium import webdriver
from common.gomeoa import GomeOa
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://office.gome.com.cn/#/portal-site/103/personal")

def isElementExist(value):
    try:
        driver.find_element_by_xpath(value)
        return True
    except:
        return False

def re_login():
    flag = isElementExist()
    if flag:
        driver.refresh()
        msg_text = driver.find_element_by_xpath("//div[@class='el-dialog__body']/span").text
        if msg_text == '用户被踢出':
            time.sleep(60)
            driver.find_element_by_xpath("//span[@class='dialog-footer']").click()
            GomeOa().login()
        else:
            driver.find_element_by_xpath("//span[@class='dialog-footer']").click()
            GomeOa().login()

    else:
        print("no")

if __name__ == '__main__':
    value = "//div[@aria-label='提示']"