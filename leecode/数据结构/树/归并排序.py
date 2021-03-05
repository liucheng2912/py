def Msearch(alist):
    if len(alist)<=1:
        return alist
    mid=len(alist)//2
    left = Msearch(alist[:mid])
    right = Msearch(alist[mid+1:])
    merge=[]
    while left and right:
        if left[0]<right[0]:
            merge.append(left.pop(0))
        else:
            merge.append(right.pop(0))
    merge.extend(right if right else left)
    return merge