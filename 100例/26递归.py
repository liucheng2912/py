"""
利用递归方法求5!。
思路：
递归三要素 结束条件 循环条件 调用
n! n*(n-1)!
n=1 1
n=2 2
"""
def fun(n):
    if n==1:
        return 1
    return n*fun(n-1)


print(fun(5))