def f(n):
    s={}
    def f1(n):
        if n in s:
            return s[n]
        else:
            if n<=1:result=n
            else:
                result=f1(n-1)+f1(n-2)
            s[n]=result
            return result
    return f1(n)

n=10
print(f(n))