def order2(l1,target):
    i,j=0,len(l1)-1
    while i<j:
        m=(i+j)//2
        if target>l1[m]:
            i=m+1
        elif target<l1[m]:
            j=m
        elif target==l1[m]:
            return True
        else:
            return False
    return False

