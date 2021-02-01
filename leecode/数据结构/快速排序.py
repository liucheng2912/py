'''
选取一个基准，大于这个基准的放一边，小于这个基准的放另一边
然后对两边的内容递归快速排序
时间复杂度O(nlogn)
'''
def order(l1):
    l2=[]
    l3=[]
    if len(l1)<2:
        return l1
    #选取中间值做基准
    mid=l1[len(l1)//2]
    #从原列表中移除基准
    l1.remove(mid)
    #遍历l1，若小于基准，放入l2，大于基准，放入l3
    for i in l1:
        if i<mid:
            l2.append(i)
        else:
            l3.append(i)
    #使用迭代进行比较
    return order(l2)+[mid]+order(l3)

print(order([11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 44, 22]))