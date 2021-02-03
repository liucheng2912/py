"""
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
思路：
引入reduce 进行相加
规律 前一个的分子是第二个的分母 前一个分子分母相加等于第二个分子
"""
from functools import reduce
l=[]
m=2
n=1
l.append(m/n)
for i in range(1,20):
    n,m=m,m+n
    l.append(m/n)

sum = reduce(lambda x,y:x+y,l)
print(sum)