# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 11:43
# @Author  : Wang Bingyin
# @Email   : xxxxxxx@163.com
# @File    : test.py
# @Software: PyCharm
import os
import time
import pathlib
from common.batepath import logs_dir

class ApprovalForm():

    @staticmethod
    def getwindows(driver):
        time.sleep(5)
        handles = (driver.window_handles)  # 获取当前窗口句柄集合（列表类型）
        for handle in handles:  # 切换窗口
            if handle != driver.current_window_handle:
                driver.switch_to_window(handle)
                break

    def read_file(self, filename, txtPayProNo):
        filename = pathlib.Path(filename)
        if filename.exists():
            #判断文件中是否存在重复的付款建议号
            with open(filename, encoding='utf-8') as rf:
                for line in rf.readlines():
                    if txtPayProNo not in line:
                        return True
                    else:
                        return False
        else:
            return True

    def write_file(self, txtPayProNo=None, str1=None):
        # 将处理结果写入文档
        filename = os.path.join(logs_dir, '{0}.txt'.format(ApprovalForm.get_current_day()))
        if self.read_file(filename, txtPayProNo):
            file = open(file=filename, mode='a+', encoding='utf-8')
            file.write(str1)
            file.close()

    @staticmethod
    def get_current_day():
        return time.strftime("%Y%m%d", time.localtime(time.time()))

    @staticmethod
    def do_Oa(driver):
        # 获取主送范围文本内容
        af = ApprovalForm()
        af.getwindows(driver)
        time.sleep(3)
        try:
            # 获取OA单号
            blSnno = driver.find_element_by_id("lblSnno").text
            # 获取付款建议号
            txtPayProNo = driver.find_element_by_id("txtPayProNo").text
        except Exception as e:
            print("OA单号或付款建议号未找到。")
            raise e
        if txtPayProNo == "":
            str1 = "付款建议号为空：{0}----OA单号:{1}.\n".format(
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), blSnno)
            print(str1)
            af.write_file(txtPayProNo, str1)
            driver.close()
            return False
        else:
            # 判断主送范围为"I"开头则送签，否则返回
            if txtPayProNo[0] == "I":
                print(txtPayProNo, ":付款建议号\"I\"开头需要送签")
                toolbarMoveTo = driver.find_element_by_id("toolbarMoveTo")
                driver.execute_script("arguments[0].click();", toolbarMoveTo)
                str1 = "送签成功：{0}----OA单号:{1}----{2}。\n".format(
                       time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), blSnno, txtPayProNo)
                print(str1)
                af.write_file(txtPayProNo, str1)
                return True
            else:
                str1 = "付款建议号非\'I\'开头：{0}----OA单号:{1}----{2}。\n".format(
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), blSnno, txtPayProNo, )
                print(str1)
                af.write_file(txtPayProNo, str1)
                driver.close()
                return False

