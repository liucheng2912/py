'''
思路：
    比较nums，若为偶数，操作 若为奇数减一再操作
'''
def f(num):
    temp=0
    while num>0:
        if num%2==0:
            temp+=1
            num=num//2
        else:
            num=num-1
            temp+=1
    return temp

num=8
print(f(num))
