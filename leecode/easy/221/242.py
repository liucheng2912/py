'''
思路：
    1、直接排序，判断元素是否相等
    2、通过字典，判断元素类型和个数
'''
def isAnagram(s,t):
    m={}
    if len(s)==0:
        if len(t)==0:return True
        else:return False
    for i in s:
        if i not in m:
            m[i]=1
        else:
            m[i]+=1
    for i in t:
        if i not in m:
            return False
        else:
            m[i]-=1
    for i in m:
        if m[i]!=0:
            return False
    return True

s = "ab"
t = "a"
print(isAnagram(s, t))
