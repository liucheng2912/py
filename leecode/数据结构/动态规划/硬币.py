'''
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，
编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)
动态规划
'''
n=25
nums={}
nums[0]=0
for i in range(1,5):
    nums[i]=1
for i in range(5,10):
    nums[i]=2
nums[10]=10
for i in range(11,n+10):
    nums[i] = nums[i - 1] + nums[i - 5]+nums[i-10]
print(nums[14])
