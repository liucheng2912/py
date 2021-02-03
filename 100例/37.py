"""
对10个数进行排序
思路：
1、sort函数
2、for循环 每次找到最新的放入列表 使用min值 用一个新的列表来进行存储 选择排序
3、冒泡排序
4、二分法排序
"""
l=[12,3,15,2,4,88,120,21,31,11]
l.sort()
print(l)

l2=[12,3,15,2,4,88,120,21,31,11]
l1=[]
while len(l2)!=0:
    min=l2[0]
    for i in l2:
        if min>i:
            min=i
    l1.append(min)
    l2.remove(min)
print(l1)

