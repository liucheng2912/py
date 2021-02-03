"""
暂停一秒输出，并格式化当前时间
思路：
time sleep暂停
time localtime 当前时间
time.time
time.strftime 格式化
"""
import time
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
time.sleep(1)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

