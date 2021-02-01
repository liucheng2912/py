#每次遍历找到最大值，然后记录下来，跟最后一个位置的交换
#复杂度O(n^2)
def order4(l1):
    for i in range(len(l1),0,-1):
        temp=0
        for j in range(0:i):
            if l1[temp]<l1[j]
                temp=j
        l1[i],l1[temp]=l1[temp],l1[i]
    return l1