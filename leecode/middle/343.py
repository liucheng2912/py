'''
dp[k]=max(i*(k-i),i*dp[k-i])
'''
def f(k):
    dp=[0]*(k+1)
    dp[0],dp[1]=0,0

    for j in range(2,k+1):
        temp1=0
        temp2=0
        for i in range(1, j):
            temp1=max(temp1,i*(j-i))
            temp2=max(temp2,i*dp[j-i])
            dp[j]=max(temp1,temp2)
    return dp[k]

k=2
print(f(k))