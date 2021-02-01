def get1(nums):
    if len(nums)<=1:return False
    dict={}
    for i in nums:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
        if dict[i]>1:
            return True
    return False


nums=[1,1,1,3,3,4,3,2,4,2]
print(get1(nums))