nums=[-2,1,-3,4,-1,2,1,-5,4]

def max1(nums):
    #动态规划实现
    #原地修改数组
    sum=nums[0]
    for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i]=+nums[i-1]
            sum=max(sum.nums[i])
    return sum

print(max1(nums))

