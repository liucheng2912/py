'''
思路：
    根据单元数量排序，优先装大单元数量的箱子
'''
def maximumunits(boxtypes,truckSize):
    s={}
    temp=0
    for i in boxtypes:
        if i[1] not in s:
            s[i[1]]=i[0]
        else:
            s[i[1]]+=i[0]
    while truckSize>0 and len(s)>0:
        max1 = max(s.keys())
        if s[max1]<truckSize:
            temp+=s[max1]*max1
            truckSize=truckSize-s[max1]
            s.pop(max1)
        else:
            temp+=max1*truckSize
            truckSize=0
    return temp

boxTypes = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
truckSize = 35
print(maximumunits(boxTypes, truckSize))
