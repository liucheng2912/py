"""
输出乘法口诀表
思路：
二维数组列表
缺点：
直接输出
二维数组实现？
乘法表第二个数的大小限制
"""
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(i,j,i*j))
