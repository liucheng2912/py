def bsearch(alist):
    for i in range(len(alist)-1,0,-1):
        temp=0
        for j in range(i):
            if alist[j]>alist[temp]:
                temp=j
        alist[i],alist[temp]=alist[temp],alist[i]
    return alist
