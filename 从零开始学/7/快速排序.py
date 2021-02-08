"""
思路：
选取一个元素，进行比较，小于的放左边left 大于的方右边 right
然后对left和right进行递归排序
结束条件
左边元素只有一个
右边元素只有一个
"""
l=[10,30,4,1,90,72,31,12,14]

def div1(l):
    div2(l,0,len(l))

def div2(l,first,last):
    if first<last:
        mid=div3(l,first,last)
    div2(l,first,mid)
    div2(l,mid+1,last)

def div3(l,first,last):
    mid=l[first]
    left=first+1
    right=last
    done=False
    while not done:
        while left<right and l[left]<=mid:
            left+=1
        while left<right and l[right]>=mid:
            right-=1
        if left>right:
            done=True
        else:
            l[left],l[right]=l[right],l[left]
    l[first],l[right]=l[right],l[first]
    return right
