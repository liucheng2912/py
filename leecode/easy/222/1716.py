'''
思路：
    if n<7 return sum(range(1,8))
    else:
        temp=n//7
        for i in range(1,temp):

'''
def tota(n):
    if n<=7:return sum(range(1,n+1))
    else:
        temp=n//7
        sum1=0
        for i in range(1,temp+1):
            sum1+=sum(range(i,i+7))
        n = n-temp*7
        sum1+=sum(range(temp+1,temp+1+n))
    return sum1

n=20
print(tota(n))