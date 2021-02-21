def QSearch(alist):
    return Q1Search(alist,0,len(alist)-1)

def Q1Search(alist,first,last):
    if first<last:
        mid=M(alist,first,last)
        return Q1Search(alist,first,mid)+mid+Q1Search(alist,mid+1,last)

def M(alist,first,last):
    mid=alist[first]
    left=first+1
    right=last-1
    done=False
    while not done:
        while left<right and alist[left]<=mid:
            left=left+1
        while right>left and alist[right]>mid:
            right-=1
        if left>right:
            done=True
        else:
            alist[left],alist[right]=alist[right],alist[left]
    return right