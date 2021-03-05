"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
思路：
1、递归
2、利用字典
"""
def f(n):
    if n<2:
        return 1
    a={}
    a[1]=1
    a[2]=2
    for i in range(3,n+1):
        a[i]=a[i-1]+a[i-2]
    return a[n]

#递归的缺点，数据量大的情况会计算很多次重复内容
def f1(n):
    if n==1:
       return 1
    if n==2:
        return 2
    return f1(n-1)+f(n-2)

n=100
print(f(n))
n=0
print(f(n))