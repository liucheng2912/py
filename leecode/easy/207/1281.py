'''
思路：
    将整数换算成数字列表
    然后进行计算
    引入functools
'''
from functools import reduce

def mul(x,y):
    return x*y
def f(n):
    a=[]
    x,y=divmod(n,10)
    if n<10:
        result=0
    else:
        while x!=0:
            x, y = divmod(n,10)
            a.append(y)
            n=x
    result = reduce(mul,a)-sum(a)
    return result

n=4421
print(f(n))