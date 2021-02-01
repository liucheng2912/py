#一个数组存奇数 一个数组存偶数 然后相加
def exchange(nums):
    l2=[]
    l1=[]
    for i in nums:
        if i%2==0:
            l2.append(i)
        else:
            l1.append(i)
    return l1+l2
#双指针法
def exchange1(nums):
    i,j=0,len(nums)-1
    while i<j:
        #找到奇数时向中间走
        while i<j and nums[i]&1==1:i+=1
        #找到偶数时向中间走
        while i<j and nums[j]&1==0:j-=1
        nums[i],nums[j]=nums[j],nums[i]
    return nums

