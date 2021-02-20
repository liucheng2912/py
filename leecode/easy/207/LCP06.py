'''
思路：
    遍历数组
    进行计算 num//2
    if num%2!=0:temp+=1
'''
def f(coins):
    temp=0
    for n in coins:
        temp+=n//2
        if n%2!=0:
            temp+=1
    return  temp

a=[2,3,10]
print(f(a))
