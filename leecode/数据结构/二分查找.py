#有序表-若大于中间值，往右找，若小于中间值，往左找
#复杂度O(logn)
#递归法实现
def DivSearch(alist,item):
    alist=list['']
    mid=len(alist)//2
    if alist[mid]>item:
        DivSearch(alist[mid+1:],item)
    elif alist[mid]<item:
        DivSearch(alist[:mid],item)
    elif alist[mid]==item:
        return True
    else:
        return False