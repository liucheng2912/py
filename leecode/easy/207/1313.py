'''
思路：
    遍历数组进行计算
    2*i+1=len(nums)
'''
def f(nums):
    l=[]
    for i in range(len(nums)//2):
        fre=nums[2*i]
        val=nums[2*i+1]
        for i in range(fre):
            l.append(val)
    return l

nums = [1,1,2,3]
print(f(nums))
