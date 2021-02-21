'''
基线：列表只有一个元素
递归条件：计算列表中除第一个元素外的其他元素的最大值，将其与第一个数字进行比较，再返回结果
'''
def max_find(l):
    max1=0
    if len(l)==1:max1=l[0]
    else:
        max1=max(l[0],max_find(l[1:]))
    return max1

l=[1,2,3,4]
print(max_find(l))