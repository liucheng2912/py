"""
斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
缺点：
递归
写法
结束条件
循环条件
"""
def f(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)


print(f(10))
