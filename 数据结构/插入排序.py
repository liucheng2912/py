def isearch(alist):
    for i in range(1,len(alist)):
        currentvalue = alist[i]
        position = i
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position=position-1
        alist[position]=currentvalue