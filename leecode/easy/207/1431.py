"""
思路：
选出数组最大值
遍历数组计算最大值减去值后，是否小于等于extra值
"""
def f(n,m):
    l=[]
    result=max(n)
    for i in n:
        if result-i<=m:
            l.append(True)
        else:
            l.append(False)
    return l

candies = [4,2,1,1,2]
extraCandies = 1
print(f(candies, extraCandies))