'''
思路：
    遍历数组 取数组a=nums0 b=nums1 c=nums2 首先c++ 判断是否有符合的元素
    假如符合 将三个元素放入数组 并将index放入set中
    假如不符合 b++ c=b+1 c++
'''
def threeSum(nums):
    if len(nums)<3:return []
    res={}
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[k]==0:
                    tmp=[nums[i],nums[j],nums[k]]
                    tmp.sort()
                    temp=0
                    for x in res:
                        if res[x]==tmp:
                            temp=1
                            break
                    if temp!=1:
                        res[i]=tmp
    res1=[]
    for i in res.values():
        res1.append(i)
    return res1

nums = [0,0,0,0]
print(threeSum(nums))