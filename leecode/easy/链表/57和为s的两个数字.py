nums = [10,26,30,31,47,60]
target = 40
def get1(nums,target):
    i,j=0,len(nums)-1
    while i<j:
        sum=nums[i]+nums[j]
        if sum>target:
            j=j-1
        elif sum<target:
            i=i+1
        else:
            return nums[i],nums[j]

print(get1(nums,target))
