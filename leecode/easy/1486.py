"""
思路：
首先计算数组的各个元素
然后利用reduce进行异或运算
"""
from functools import reduce

def f(x,y):
    return x^y

def f1(n,start):
    nums=[]
    for i in range(n):
        nums.append(start+2*i)
    res = reduce(f,nums)
    return res

n = 10
start = 5
print(f1(n, start))