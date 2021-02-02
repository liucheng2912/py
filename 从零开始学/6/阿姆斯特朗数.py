"""
如果一个n位正整数等于各位数字n次方的和，就称该数为阿姆斯特朗数
写一个程序检测输入的数字是否是阿姆斯特朗数
思路：
1、输入
2、将输入的数字各位数字拆解然后计算n次方和
3、实现
利用divmod 获取商和余数
利用商为0 所需的次数来判断位数
"""
from functools import reduce

n=int(input('请输入数字:'))
l=[]
tmp=0
x=n
while n!=0:
    n,y=divmod(n,10)
    l.append(y)
    tmp+=1
result=0
for i in l:
    result+= i**tmp

if result==x:
    print('这是一个阿姆斯特朗数')
else:
    print('这不是一个阿姆斯特朗数')
