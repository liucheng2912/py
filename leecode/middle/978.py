'''
思路：
    k为奇数的时候，A[k]>A[k+1]
    k为偶数的时候,A[k]<A[k+1]
    or
    k为奇数的时候,A[k]<A[k+1]
    k为偶数的时候,A[k]>A[k+1]
遍历数组
假如长度<=1,直接返回数组即可
假如长度为2,只要两个值不相等即可
长度>2,遍历数组，两种比较方式，取最大值
'''
def f(arr):
    if len(arr)<=1:return 1
    elif len(arr)==2:
        if arr[0]!=arr[1]:
            return 2
    else:
        temp=0
        for i in range(1,len(arr)-1):
            pass