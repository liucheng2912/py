def get1(n,m):
    return f(n,m)


def f(n,m):
    if n==0:return 0
    x=f(n-1,m)
    return (m+x)%n

print(get1(5,3))
