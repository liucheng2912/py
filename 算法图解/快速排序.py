'''
思路：
    基线条件    列表长度为0或1，直接返回，不进行排序
    递归条件    取一个基准值，小于他的放一堆，大于他的放一堆，然后对小的进行递归排序，大的进行递归排序
'''
def quicksort(l):
    if len(l)<=1:return l
    else:
        l1=[]
        l2=[]
        temp=l[0]
        for i in l[1:]:
            if i<=temp:
                l1.append(i)
            else:
                l2.append(i)
        l3=quicksort(l1)+[temp]+quicksort(l2)
        return l3

a=[2,1,4,6,10,3,7,1]
print(quicksort(a))