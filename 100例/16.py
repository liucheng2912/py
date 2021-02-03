"""
输出指定格式的日期
思路：
time模块 strftime
localtime
优化：
datetime
"""
import time
import  datetime
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
print(time.strftime('%Y-%m-%d',time.localtime()))
print(time.strftime('%m-%d',time.localtime()))
print(time.strftime('%d/%m/%Y',time.localtime()))

print(datetime.date.today().strftime('%d%m%Y'))
