'''
思路：
    遍历字符串
    满足条件
    为I的时候，小于右边的值 以I开头的，最小值
    为D的时候，大于右边的值 以D开头的 最大值
    循环遍历即可
'''
def diStringMatch(S):
    l=[]
    n=0
    m=len(S)
    for i in S:
        if i=='I':
            l.append(n)
            n+=1
        if i=='D':
            l.append(m)
            m-=1
    while n<=m:
        l.append(n)
        n+=1
    return l

s="IDID"
print(diStringMatch(s))
s="III"
print(diStringMatch(s))
s="DDI"
print(diStringMatch(s))