def get1(nums):
    m=len(nums)
    for i in range(m):
        if i not in nums:
            return i

l1=[3,0,1]
print(get1(l1))