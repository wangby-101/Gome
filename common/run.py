# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 13:09
# @Author  : WangBingyin
# @Email   : wangbingyin-zkhtg@gome.com.cn
# @File    : run.py
# @Software: PyCharm
import time
from common.gomeoa import GomeOa

gome = GomeOa()
gome.login()

while True:
    print("开始时间:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    gome.test_all() # 审核全部单据
    print("结束时间:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    time.sleep(60*60)

