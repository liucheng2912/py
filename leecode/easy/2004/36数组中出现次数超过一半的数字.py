'''
返回数组中出现次数超过数组长度一半的元素
'''

#直接将数组排序，取中间元素，sort函数是一种归并方法的改进，时间复杂度为O(nlogn)
#空间复杂度为O(1)
def get_bysort(n):
    n.sort()
    m=len(n)//2
    return n[m]

#遍历列表，字典存放元素和出现次数，遍历需要的时间复杂度为O(n),字典取数的复杂度为O(1),
#空间复杂度为O(n)
def get_bydict(n):
    if not n:return None
    if len(n)==1:return n
    write={}
    for i in n:
        if i not in write:
            write[i]=1
        else:
            write[i]+=1
            if write[i]>(len(n)//2):
                return i
    return None

#快速排序，当前回合进行完快排后的数组下标i是否等于数组长度的一半，若是则直接返回结果
#时间复杂度为O(nlogn),空间复杂度为O(1)

if __name__=='__main__':
    n=[1, 2, 3, 2, 2, 2, 5, 4, 2]
    m1=get_bysort(n)
    m2=get_bydict(n)
    print(m1)
    print(m2)

