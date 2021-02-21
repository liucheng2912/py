'''
思路：
    1、遍历列表和字符，用字典来存放，但是没法保证每个字符的次数，只有总的次数
    2、通过遍历字符串，找出每个字符串中都出现元素的最小次数
'''
def commonChars(A):
    s={}
    for i in A[0]:
        if i not in s:
            s[i]=1
        else:
            s[i]+=1
    if len(A)>1:
        for i in range(1,len(A)):
            s1={}
            for j in A[i]:
                if j not in s1:
                    s1[j]=1
                else:
                    s1[j]+=1
            for x in s:
                if x not in s1:
                    s[x]=-1
                else:
                    s[x]=min(s[x],s1[x])
    l=[]
    for i in s:
        if s[i]!=-1:
            for j in range(s[i]):
                l.append(i)
    return l

s=["bella","label","roller"]
print(commonChars(s))
s=["cool","lock","cook"]
print(commonChars(s))



