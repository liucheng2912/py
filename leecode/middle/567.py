'''
思路：
    滑动窗口 比较字符串出现频率是否相等
'''
def checkInclusion(s1,s2):
    if len(s1)>len(s2):return False
    else:
        n1=len(s1)
        d={}
        for i in s1:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for j in range(len(s2)-n1+1):
            d1={}
            temp=0
            for i in s2[j:j+n1]:
                if i not in d1:
                    d1[i]=1
                else:
                    d1[i]+=1
            for i in d:
                if i not in d1 or d[i]!=d1[i]:
                    temp=1
                    break
            if temp!=1:
                return True
        return False
s1= "adc"
s2 = "dcda"
print(checkInclusion(s1, s2))

