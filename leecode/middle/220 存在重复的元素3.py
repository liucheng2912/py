def get1(nums,k,t):
    for i in range(len(nums)):
        for j in nums[i+1:i+k+1]:
            temp=abs(nums[i]-j)
            if temp<=t:
                return True
    return False

nums=[1,5,9,1,5,9]
k=2
t=3
print(get1(nums,k,t))