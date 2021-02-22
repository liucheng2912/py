'''
思路：
    遍历数组
    用arr1中的值 减去arr2计算abs 假如存在小于d的不符合要求
'''
def findT(arr1,arr2,d):
    cur = 0
    for i in arr1:
        temp=0
        for j in arr2:
            if abs(i-j)<=d:
                temp=1
                break
        if temp!=1:
            cur+=1
    return cur

arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
print(findT(arr1, arr2, d))

