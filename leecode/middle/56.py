'''
思路：
遍历数组 index为0  然后查找后面的元素中是否有在期间的元素 ，假如在进行合并
'''
def merge(intervals):
    n=len(intervals)
    l=[]
    n1=intervals[0][0]
    n2=intervals[0][1]
    for i in range(1,n):
        for j in
        if intervals[i][0]<=n1 and intervals[i][1]>=n1:
            temp=1
            n2=intervals[i][1]

