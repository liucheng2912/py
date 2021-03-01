'''
思路：
    遍历，利用target -i 寻找值是否在列表中
'''
def twoSum(nums,target):
    for i in range(len(nums)):
        temp=i
        target1= target-nums[i]
        for j in range(i+1,len(nums)):
            if target1 == nums[j]:
                temp1=j
                return [temp,temp1]
            if target1<j:
                break
    return []

nums = []
target = 0
print(twoSum(nums, target))