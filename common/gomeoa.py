# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 10:29
# @Author  : Wang Bingyin
# @Email   : wangbingyin-zkhtg@gome.com.cn
# @File    : gomeoa.py
# @Software: PyCharm
import time
from selenium import webdriver
from common.approvalform import ApprovalForm
from common.get_confs import Config
from common import batepath

config = Config(batepath.conf_dir)


class GomeOa(object):

    def __init__(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Ie()
        # self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def login(self):
        "登录"
        self.driver.get(config.get("Login", "url"))
        self.driver.implicitly_wait(10)
        # 定位板块和公司下拉列表元素
        companies_js = self.driver.find_element_by_xpath("//span[@class='el-input__suffix-inner']")
        self.driver.execute_script("arguments[0].click();", companies_js)
        # 选择国美电器选项
        gome_electric_js = self.driver.find_element_by_class_name("el-select-dropdown__item")
        self.driver.execute_script("arguments[0].click()", gome_electric_js)
        # self.driver.find_element_by_xpath("//input[@placeholder='账号']").send_keys("zhangruixia-bjdz")
        # self.driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys("ZHANGrui123.")
        login_btn = self.driver.find_element_by_xpath("//*[@class='el-button el-button--primary el-button--small']")
        self.driver.execute_script("arguments[0].click()", login_btn)

    def test_all(self):
        # 切换电器OA菜单
        electric_js = self.driver.find_element_by_xpath("//*[@id='tab-2,']")
        self.driver.execute_script("arguments[0].click();", electric_js)
        row = 1
        while True:
            time.sleep(5)
            next_btn = self.driver.find_element_by_xpath("//button[@class='btn-next']")
            # 获取table中tr数量
            tr_num = self.getbefore_add_numbers()
            if row > tr_num:
                if next_btn.is_enabled():
                    self.driver.execute_script("arguments[0].click();", next_btn)
                    row = 1
                else:
                    print("结束，撒花!!!")
                    break
            else:
                time.sleep(5)
                # self.driver.implicitly_wait(10)
                file_title = self.driver.find_element_by_xpath(
                    "//*[@id='pane-2,']/div/div[3]/table/tbody/tr[{0}]/td[2]".format(row)).text
                if file_title[0:11] == "国美管家商家结算申请表":
                    tr_div = self.driver.find_element_by_xpath(
                        "//*[@id='pane-2,']/div/div[3]/table/tbody/tr[{0}]".format(row))
                    self.driver.execute_script("arguments[0].click();", tr_div)
                    time.sleep(8)
                    af = ApprovalForm()
                    result = af.do_Oa(self.driver)
                    time.sleep(5)
                    self.driver.switch_to_window(self.driver.window_handles[0])
                    if result is False:
                        row += 1
                else:
                    row += 1

    def getbefore_add_numbers(self):
        # 获取table列表中所有数据条数
        # 定位到table，并返回table中tr元素长度
        menu_table = self.driver.find_element_by_xpath("//*[@id='pane-2,']/div/div[3]/table/tbody")
        rows = menu_table.find_elements_by_tag_name('tr')
        return len(rows)

    def quit_windows(self):
        # 关闭窗口
        self.driver.quit()


if __name__ == '__main__':
    gome = GomeOa()
    gome.login()
    gome.test_all()
