'''
思路：
    0 1 2 3 4
    1 2 3 1 2
    3 1   2 3
      1   2
      3
    用key和value
    value更新index 假如为m 跳过
f(n,m)  从n个数中每次删除第m个数，共删除了n-1次，最后留下的那个数的序号
f(n,m) 场景下删除的第一个数的序号是 (m-1)%n
f(n-1,m) 场景将使用被删除数字的下一个树 即序号m%n 作为它的0序号
f(n-1,m)=x  x是从f(n,m)下序号为m%n的数字出发所获得的的结果
m%n+x 是f(n,m) 场景下的结果序号
f(n,m)=(m%n+x)%n =(m+x)%n=(m+f(n-1,m))%n

'''
def f(n,m):
    if n==0:return 0
    x=f(n-1,m)
    return (x+m)%n

n=5
m=3
f(n,m)