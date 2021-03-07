def f(n):
    a=0
    b=1
    for i in range(n):
        a,b=b,a+b
    return a

n=5
print(f(n))