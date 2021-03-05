def f(s,i,j):
    if i>j:return s
    else:
        s[i],s[j]=s[j],s[i]
        return f(s,i+1,j-1)

s=["H","a","n","n","a","h"]
print(f(s, 0, 5))