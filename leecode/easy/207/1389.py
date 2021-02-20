'''
思路：
利用insert
遍历index 然后 target(index,nums[i])
'''

def f(nums,index):
    target=[]
    for i in range(len(index)):
        target.insert(index[i],nums[i])
    return target

nums = [1,2,3,4,0]
index = [0,1,2,3,0]
print(f(nums, index))