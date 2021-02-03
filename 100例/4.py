"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
思路：
2021年2月2号
首先判断年份是不是闰年 年%4==0 是的话 2月份 29天
字典存放 key:value 月份 天数
日期 直接相加
缺点：
闰年的判断
400年整除 和 4整除，100不整除
月份天数的判断
月份大于12
天数大于31
"""
y=int(input('year:'))
m=int(input('month:'))
d=int(input('date:'))
num=0
b=[31,28,31,30,31,30,31,31,30,31,30,31]
if m<1 or m>12:
    print('month illegal')
if d>31 or d<0:
    print('date illegal')
for i in range(m-1):
    num+=b[i]
num+=d
#闰年且大于2月份
if ((y%4==0 and y%100!=0) or y%400==0) and m>2:
        num+=1
print(num)



