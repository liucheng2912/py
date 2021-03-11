'''
思路：
    首先将数组排序，升序排列
    然后比较x1 y1 x2 y2 x2是否在x1 和y1之间
    假如在之间 将其变为x1 y2
'''
def merge(intervals):
    if len(intervals)==1:return intervals
    intervals.sort()
    s1=set()
    res=[]
    for i in range(len(intervals)-1):
        if i not in s1:
            s1.add(i)
            x1=intervals[i][0]
            y1=intervals[i][1]
            for j in range(i+1,len(intervals)):
                x2=intervals[j][0]
                y2=intervals[j][1]
                if x2>=x1 and x2<=y1:
                    if y2>y1:
                        y1=y2
                    s1.add(j)
            res.append([x1,y1])
    if len(intervals)-1 not in s1:
        res.append(intervals[-1])
    return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
intervals = [[1,4],[4,5]]
print(merge(intervals))