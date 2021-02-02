"""
给定一个范围内的数字，让用户猜，根据输入内容判断是否是大了还是小了，并展示猜了多少次
思路：
1、输入
2、判断输入内容
3、循环，条件判断
"""
import random
n = int(input('请输入'))
m= random.randint(0,100)
guess=0
while 1:
    if n <m:
        print("小了")
        n = int(input('请输入'))
        guess+=1
    elif n>m:
        print('大了')
        n = int(input('请输入'))
        guess += 1
    else:
        guess += 1
        print('猜对了')
        print('一共猜了%s次！'%guess)
        break