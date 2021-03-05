'''
思路：
    三角形定义
    两边之和大于第三边

'''
def f(A):
    if len(A)<3:return 0
    A.sort()
    for i in range(len(A)-1,1,-1):
        if A[i]<A[i-1]+A[i-2]:
            return A[i]+A[i-1]+A[i-2]
    return 0

A=[2,1,2]
print(f(A))