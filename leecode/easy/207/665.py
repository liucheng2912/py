'''
思路：
假如n[i]>n[i+1]
首先将n[i]替换成n[i+1] 然后比较 是否n[i-1]<n[i+1]
否则 将n[i+1]换成n[i]
'''
def f(n):
    temp=False
    for i in range(len(n)-1):
        if n[i]>n[i+1]:
            if temp:
                return False
            temp=True
            if i==0 or n[i-1]<=n[i+1]:
                n[i]=n[i+1]
            else:
                n[i+1]=n[i]
    return True




n=[1,4,1,2]
print(f(n))
