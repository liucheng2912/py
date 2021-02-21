'''
思路：
    指针
    i j
    首先计算出所有奇数长度的数组
    然后分别对奇数长度数组求和
    再求总和
'''
def f(arr):
    n=1
    sum1 = 0
    while 2*n-1<=len(arr):
        i = 0
        while i + 2 * n - 1<=len(arr):
            l=arr[i:i + 2 * n - 1]
            i+=1
            sum1 += sum(l)
        n+=1
    return sum1

arr = [10,11,12]
print(f(arr))
