"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
思路：
爬n阶的方案为n-1阶和n-2阶的和
假如n=1 为1
假如n=2 为2
"""
def f(n):
    s={}
    def f1(n):
        if n in s:
            return s[n]
        else:
            if n<=2:
                result=n
            else:
                result=f1(n-1)+f1(n-2)
            s[n]=result
            return result
    return f1(n)

n=10
print(f(n))