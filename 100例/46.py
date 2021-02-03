"""
求输入数字的平方，如果平方运算后小于 50 则退出。
"""


def f(n):
    sum=n**2
    if sum<50:
        return

    else:
        print(sum)
        return sum
if __name__=='__main__':
    n = int(input())
    f(n)