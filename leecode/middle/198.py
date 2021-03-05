'''
思路：
    dp[n]=max(dp[n-1],dp[n-2]+n)
'''


def rob(nums):
    dp = {}
    dp[0] = 0
    if len(nums)>0:dp[1] = nums[0]
    for i in range(2, len(nums) + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

    return dp[len(nums)]

nums=[]
print(rob(nums))