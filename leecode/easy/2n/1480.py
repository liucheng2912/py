"""
思路：
利用functools reduce
双重for循环
"""
from functools import reduce
def add1(x,y):
    return x+y
def f(s):
    l=[]
    for i in range(len(s)):
        if i==0:l.append(s[i])
        else:
            s1=s[:i+1]
            l.append(reduce(add1,s1))
    return l

nums = [3,1,2,10,1]
print(f(nums))