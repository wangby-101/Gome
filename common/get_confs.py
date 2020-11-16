# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 18:08
# @Author  : Wang Bingyin
# @Email   : xxxxxxx@163.com
# @File    : get_confs.py
# @Software: PyCharm

import os
from configparser import ConfigParser
from common import batepath
class Config:

    def __init__(self, filename):
        self.conf = ConfigParser()
        self.conf.read(filenames=filename)
        online = os.path.join(batepath.conf_dir, "conf.conf")
        self.conf.read(online, encoding="utf-8")
        # print(self.conf.get("Login", "url"))


    def get(self, section, option): # 返回字符串格式
        return self.conf.get(section=section, option=option)

    def getboolean(self, section, option): # 返回布尔值
        return self.conf.getboolean(section=section, option=option)

    def getint(self, section, option): # 返回int格式
        return self.conf.getint(section=section, option=option)

    def getfloat(self, section, option): # 返回浮点型格式
        return self.conf.getfloat(section=section, option=option)


if __name__ == '__main__':
   conf = Config(batepath.conf_dir)
   print(conf.get("Login", "name"))
   print(conf.get("Login", "pass"))