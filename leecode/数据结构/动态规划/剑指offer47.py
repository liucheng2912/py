'''
思路：
    最优算法
    遍历第一行 加上右边或者下边的最大值
'''
def m(grid):
    n= len(grid[0])
    m=len(grid)
    tmp=0
    for i in range(n):
        k=i
        j=0
        tmp1=grid[k][j]
        while k+1<n and j+1<m:
            if grid[k+1][j]>grid[k][j+1]:
                tmp1+=grid[k+1][j]
                k+=1
            else:
                tmp1+=grid[k][j+1]
                j+=1
        if j<m:
            tmp1+=grid[k][j+1]
            j+=1
        if k<n:
            tmp1+=grid[k+1][j]
            k+=1
        tmp=max(tmp,tmp1)
    return tmp

grid=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(m(grid))
