'''
思路：
    找出最大的两个元素，进行求和
'''
def f(nums):
    if len(nums)==1:return nums[0]
    if len(nums)==2:return (nums[0]-1)*(nums[1]-1)
    else:
        temp1=max(nums)
        nums.remove(temp1)
        temp2=max(nums)
        return (temp1-1)*(temp2-1)

nums = [3,4,5,2]
print(f(nums))