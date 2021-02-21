def f(s):
    temp=0
    l=[]
    for i in range(len(s)):
        temp+=s[i]
        l.append(temp)
    return l

nums = [1,1,1,1,1]
print(f(nums))