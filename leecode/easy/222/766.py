'''
思路：
    1、对角线元素的定位
    下一行对应元素为当前行元素的列数+1
    遍历矩阵
    2、填充元素然后比较每列元素是否相等
    1234
    5123
    9512
    001234
    051230
    951200
    3、前行去除最后一个元素 和后行去除第一个元素 完全相等
'''
def isT(matrix):
    n=1
    m=len(matrix[0])
    while n<len(matrix):
        s1=matrix[n-1]
        s2=matrix[n]
        if s1[:m-1]!=s2[1:]:
            return False
        else:
            n+=1
    return True


matrix = [[1,2],[2,2]]
print(isT(matrix))






