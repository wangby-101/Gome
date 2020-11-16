# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 17:18
# @Author  : Wang Bingyin
# @Email   : xxxxxxx@163.com
# @File    : timer.py
# @Software: PyCharm
import os
from common.batepath import logs_dir, count_file
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

class Timer():
    def __init__(self):
        self.scheduler = BlockingScheduler()

    # 每周五统计上周五-本周四处理的OA数量
    @staticmethod
    def count_job():
        now = datetime.now().strftime("%Y%m%d")
        succeed_list = []
        untreated_list = []
        for i in range(1, 8):
            file_name = os.path.join(logs_dir, '{}.txt'.format(int(now) - i))
            if os.path.exists(file_name):
                with open(file_name, mode='r', encoding='utf-8') as file:
                    for line in file.readlines():
                        line = line.strip('\n')
                        if line[0:4] == '送签成功':
                            succeed_list.append(line)
                        else:
                            untreated_list.append(line)
                    file.close()
            else:
                continue

        # 将统计结果写入文件
        count_text = "统计时间：{0}----处理成功数量：{1}\n".format(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),len(succeed_list))
        print(count_text)
        cf = open(count_file, mode='a+', encoding='utf-8')
        cf.write(count_text)
        cf.close()

    def add_jobs(self, job):
        # 添加 job
        self.scheduler.add_job(job, "cron", day_of_week="fri", hour=17, minute=30)
        # 启动
        self.scheduler.start()

if __name__ == '__main__':
    timer = Timer()
    timer.add_jobs(timer.count_job)