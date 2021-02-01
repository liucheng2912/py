'''
将一个数组通过中间值，拆分为2分，再继续拆分2分，直到不能拆分
将拆分后的子集逐渐合并
时间复杂度O(nlogn)
'''
def order(l1):
    if len(l1)<=1:
        return l1
    mid=len(l1)//2
    left=l1[:mid]
    right=l1[mid:]
    return marge(order(left),order(right))#拆分

#合并两个数列
def marge(l1,l2):
    result=[]
    #两个数列都有值
    while len(l1)>0 and len(l2)>0:
        #左右两个数列中第一个最小放前面，放了之后直到一个列表中的值空了
        if l1[0]<l2[0]:
            result.append(l1.pop(0))
        else:
            result.append(l2.pop(0))
    #只有一个数列中还有值，直接添加
    result+=l1
    result+=l2
    return result

a=order([11, 99, 33 , 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22])
print(a)