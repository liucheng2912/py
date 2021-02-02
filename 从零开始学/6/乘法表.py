"""
输出九九乘法表
"""
for i in range(1,10):
    sum=[]
    if i==1:
        sum.append(1)
    else:
        for j in range(1,i):
            sum.append(i*j)
    print(sum)

