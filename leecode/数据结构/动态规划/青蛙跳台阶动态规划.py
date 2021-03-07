def numWays(n: int):
    a = 1
    b = 2
    for _ in range(1, n):
        a, b = b, a + b
    return a % 1000000007

n=2
print(numWays(n))