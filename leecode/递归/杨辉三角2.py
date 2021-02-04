def f(n):
    if n==1:return [1]
    if n==2:return [1,1]
    pre=f(n-1)
    l=[1]
    for j in range(len(pre)-1):
        l.append(pre[j]+pre[j+1])
    l.append(1)
    return l
n=10
print(f(n))