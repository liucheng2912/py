"""
思路：
    找出两个数组相同的元素
    使用字典存放一个数组，然后遍历另一个数组
"""
def f(nums1,nums2):
    d={}
    l=[]
    for i in nums1:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in nums2:
        if i in d:
            l.append(i)
            d[i]-=1
            if d[i]==0:
                d.pop(i)
    return l

nums1 = [1,2,2,1]
nums2 = [2,2]
print(f(nums1, nums2))

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(f(nums1, nums2))