'''
题意：交换每个元素的行和列
思路：
    利用一个新的矩阵，然后读取这个矩阵中的元素
'''
def f(martix):
    #行
    m=len(martix)
    #列
    n=len(martix[0])
    s1=[[None for i in range(m)]for j in range(n)]
    for i in range(n):
        for j in range(m):
            s1[i][j]=martix[j][i]
    return s1

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(f(matrix))
