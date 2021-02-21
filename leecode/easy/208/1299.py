'''
思路：
    数组分片，查找出最大值，然后进行入组
'''
def f(arr):
    if len(arr)==1:return [-1]
    else:
        l=[]
        for i in range(len(arr)-1):
            l.append(max(arr[i+1:]))
        l.append(-1)
        return l

arr = [17,18,5,4,6,1]
print(f(arr))
arr = [400]
print(f(arr))