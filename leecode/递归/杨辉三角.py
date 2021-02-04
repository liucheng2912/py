"""
递归实现
每行 f(n)=[1,f(n-1),1] l.append(f(n))
结束条件
n=1 f(1)=[1]
n=2 f(2)=[1,1]
"""
def f1(n):
    def f(n):
        if n==1:return [1]
        if n==2:return [1,1]
        tmp=[1]
        pre=f(n-1)
        for j in range(len(pre)-1):
            tmp.append(pre[j]+pre[j+1])
        tmp.append(1)
        return tmp
    l=[]
    for i in range(1,n+1):
        tmp=f(i)
        print(tmp)
        l.append(tmp)

n=10
f1(n)

