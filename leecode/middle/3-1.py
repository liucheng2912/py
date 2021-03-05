def fA(s):
    left=0
    right=0
    res=0
    d1=set()
    while right<len(s):
        if s[right] not in d1:
            d1.add(s[right])
            right += 1
            res = max(res, len(d1))
        else:
            d1.remove(s[left])
            left+=1
        res=max(res,len(d1))
    return res

s='pwwkew'
print(fA(s))
