def order2(l1,target):
    i,j=0,len(target)-1
    while i<j:
        m=(i+j)//2
        if target>l1[m]:
            return order2(l1[m+1:],target)
        elif target<l1[m]:
            return order2(l1[:m],target)
        elif target==l1[m]:
            return True
    return False