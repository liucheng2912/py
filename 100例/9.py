"""
暂停一秒输出
思路:
sleep函数
缺点：
没有考虑到模块引入
sleep属于time模块
"""
from time import sleep
for i in range(9):
    print(i)
    sleep(1)