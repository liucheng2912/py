'''
思路：
    通过哈希表来实现
'''
def intersection(nums1,nums2):
    s1=set(nums1)
    s2=set(nums2)
    l=[]
    for i in s2:
        if i in s1:
            l.append(i)
    return l

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1, nums2))
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))
