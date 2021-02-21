'''
思路：
    矩阵元素遍历
    if i==j:
        mat[i][j]
'''
def f(mat):
    n=len(mat)
    sum=0
    for i in range(n):
        for j in range(n):
            if i==j or i+j==n-1:
                sum+=mat[i][j]
    return sum

mat2 = [[1,2,3],[4,5,6], [7,8,9]]
mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
mat1=[[5]]
print(f(mat))
print(f(mat1))
print(f(mat2))