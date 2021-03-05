def climbStairs(n):
    dp={}
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

def climbStairs1(n):
    if n==1 or n==2:return n
    pre1,pre2=1,2
    for i in range(3,n+1):
        pre1,pre2=pre2,pre1+pre2
    return pre2

