def findMaxConsecutiveOnes(nums):
    left,right=0,0
    res=0
    sum=0
    N=len(nums)
    while right<N:
        if nums[right]==nums[left] and nums[right]==1:
            sum+=1
            right+=1
        else:
            sum=0
            left=right
            if nums[right]==0:
                right+=1
            else:
                right=right
        res=max(res,sum)
    return res


a=[1,1,0,1,1,1]
print(findMaxConsecutiveOnes(a))