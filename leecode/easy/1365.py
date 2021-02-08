'''
思路：
    双重遍历
'''
def f(nums):
    a=[]
    for x in nums:
        temp=0
        nums1=nums[:]
        nums1.remove(x)
        for y in nums1:
            if x>y:
                temp+=1
        a.append(temp)
    return a

nums = [6,5,4,8]
print(f(nums))

