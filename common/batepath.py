# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 18:09
# @Author  : Wang Bingyin
# @Email   : xxxxxxx@163.com
# @File    : batepath.py
# @Software: PyCharm

import os
# 基础路径
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 配置文件路径
conf_dir = os.path.join(base_dir, 'confs')
conf_file = os.path.join(conf_dir, 'conf.conf')
# log
logs_dir = os.path.join(base_dir, 'logs')
count_file = os.path.join(logs_dir, 'count_results.txt')

if __name__ == '__main__':

    print(conf_dir)
