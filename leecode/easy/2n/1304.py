'''
思路：
    一个n
    若是偶数，直接用n//2
    若是奇数，用0填充
'''
def sumZero(n):
    l=[]
    for i in range(1,n//2+1):
        l.append(-1*i)
    for i in range(1,n//2+1):
        l.append(i)
    if n%2==0:
        return l
    else:
        l.append(0)
        return l

n=5
print(sumZero(n))
