'''
思路：
    1、遍历，排序
    2’插入排序？
'''
def relativeSortArray(arr1,arr2):
    arr3=arr2[:]
    arr4=[]
    for i in arr1:
        temp=0
        for j in arr2:
            if i==j:
                index = arr2.index(j)
                arr2.insert(index+1,i)
                temp=1
                break
        if temp==0:
            arr4.append(i)
    arr4.sort()
    for i in arr3:
        if i in arr2:
            arr2.remove(i)
    return arr2+arr4

arr1=[3,3,2,6,7,9,19]
arr2=[3,9,6]
print(relativeSortArray(arr1, arr2))