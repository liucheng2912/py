def f(n):
    l=[]
    def f1(n):
        if n==1:return [1]
        if n==2:return [1,1]
        else:
            s=[1]
            pre=f1(n-1)
            for i in range(len(pre)-1):
                s.append(pre[i]+pre[i+1])
            s.append(1)
        return s
    for i in range(1,n+1):
        l.append(f1(i))
    return l

n=10
print(f(n))