'''
思路：
    双指针 滑动窗口
'''
def f(s):
    if len(s)<=1:return len(s)
    i=0
    j=0
    tmp=0
    s1=set()
    while j<len(s):
        if s[j] not in s1:
            s1.add(s[j])
            j+=1
            tmp = max(tmp, j - i)
        else:
            s1.remove(s[i])
            i+=1
    return tmp

s="abcabcbb"
print(f(s))


