def numWays(n: int) -> int:
    a = {}
    if n<2:
        return 1
    a[1]=1
    a[2]=2
    for i in range(3, n + 1):
        a[i] = a[i - 1] + a[i - 2]
    return a[n]%1000000007


print(numWays(100))