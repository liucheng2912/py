'''
如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。
如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。
'''
import math
def f(s,t,cost):
    left=0
    right=0
    res=0
    temp=0
    N=len(s)
    while right<N:
        temp+= abs(ord(s[right])-ord(t[right]))
        right+=1
        while temp>cost:
            temp-=abs(ord(s[left])-ord(t[left]))
            left+=1
        res = max(res,right-left)
    return res

s = "abcd"
t = "bcdf"
cost = 3
print(f(s, t, cost))
