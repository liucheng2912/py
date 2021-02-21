'''
思路：
    查找元素，同一行中最小，同一列中最大
    暴力法：
    遍历数组 找出每行最小的元素
    遍历数组，找出每列最大的元素
    相等即找到幸运数
'''
def f(matrix):
    m=len(matrix)
    n=len(matrix[0])
    l1=set()
    for i in range(m):
        l1.add(min(matrix[i]))
    for i in range(n):
        max1=0
        for j in range(m):
            if max1<matrix[j][i]:
                max1=matrix[j][i]
        if max1 in l1:
           return [max1]
    return []

matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(f(matrix))




