"""
time.asctime() 国外的时间格式
time.time() 时间戳
time.sleep() 等待
time.localtime() 时间戳转成时间元组
time.strftime() 将当前的时间戳转成带格式的时间

"""
import time
#国外时间
print(time.asctime())
#时间戳
print(time.time())
#时间元组
print(time.localtime())
#转换成带格式的时间 第二个参数需要是tuple
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

#获取两天前的时间
now_timestamp=time.time()
two_day_before=now_timestamp - 60*60*24*2
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(two_day_before)))