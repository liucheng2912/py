"""
判断输入的年份是否是闰年
思路：
1、输入
2、判断 整除400 和 整除4但不能整除100的年份为闰年
3、实现
    判断语句
"""
n=int(input("请输入年份"))
if n%400==0 or (n%4==0 and n%100!=0):
    print('%d是闰年'%n)
else:
    print('%d不是闰年'%n)