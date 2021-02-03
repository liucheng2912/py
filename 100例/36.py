"""
求一百以内的素数
思路：
素数定义：除了1和自身，不能被2到自身-1的范围内整除 素数大于1
利用for循环
"""
l=[]
for i in range(2,100):
    temp=0
    if i==2:
        pass
    for j in range(2,i):
        if i%j==0:
            temp=1
            break
    if temp==0:
        l.append(i)
print(l)
