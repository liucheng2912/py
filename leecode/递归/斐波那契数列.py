def f1(n):
    s={}
    def f(n):
        if n in s:
            return s[n]
        else:
            if n<=1:
                result=n
            else:
                result=f(n-1)+f(n-2)
            s[n]=result
            return result
    return f(n)

n=10
print(f1(10))
