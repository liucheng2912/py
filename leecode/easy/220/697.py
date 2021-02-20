'''
思路：
    首先找出元素出现次数最多的元素 s.count
    然后找出包含所有元素的最短字段
    首先是以这个元素开头，以这个元素结尾 然后长度需要大于等于最多次数
'''
def findShortestSubArray(nums):
    s={}
    minlen=len(nums)
    for i in nums:
        if i not in s:
            s[i]=1
        else:
            s[i]+=1
    max1=max(s.values())
    if max1==1:return 1
    else:
        for i in s:
            if s[i]==max1:
                n=nums.index(i)
                counter=0
                temp=0
                while n<len(nums) and temp<max1:
                    if nums[n]==i:
                        temp+=1
                    counter+=1
                    n+=1
                minlen=min(minlen,counter)
    return minlen



nums=[1, 2, 2, 3, 1]
print(findShortestSubArray(nums))
nums=[1,2,2,3,1,4,2]
print(findShortestSubArray(nums))






