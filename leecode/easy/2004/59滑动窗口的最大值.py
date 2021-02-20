def get1(nums,k):
    l1=[]
    i,j=0,k
    while j<=len(nums):
        sum=nums[i]
        for temp in range(i,j):
            if sum<nums[temp]:
                sum=nums[temp]
        l1.append(sum)
        i+=1
        j+=1
    return l1

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(get1(nums,k))


