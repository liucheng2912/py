'''
思路：
    遍历字符串
    两个列表，一个列表存放字符，一个列表存放次数
    字典存放字符和出现次数
'''
def f(s):
    d={}
    s1=''
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    s=list(set(s))
    s.sort()
    while len(d)>0:
        for i in s:
            if i in d:
                s1+=i
                d[i]-=1
                if d[i]==0:
                    d.pop(i)
        for i in range(len(s)-1,-1,-1):
            if s[i] in d:
                s1+=s[i]
                d[s[i]]-=1
                if d[s[i]]==0:
                    d.pop(s[i])
    return s1

s = "leecode"
print(f(s))






