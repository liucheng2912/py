def longestOnes(A,K):
    left,right=0,0
    res=0
    zeros=0
    N=len(A)
    while right<N:
        if A[right]==0:
            zeros+=1
        while zeros>K:
            if A[left]==0:
                zeros-=1
            left+=1
        res=max(res,right-left+1)
        right+=1
    return res

A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
print(longestOnes(A, K))
