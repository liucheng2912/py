'''
思路：
    循环计算
'''
def f(n):
    temp=0
    while n>1:
        if n%2==0:
            n=n//2
            temp+=n
        else:
            n1=(n-1)//2
            n = (n - 1) // 2+1
            temp+=n1
    return temp

n=14
print(f(n))