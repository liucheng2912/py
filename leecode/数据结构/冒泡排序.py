def order3(l1):
    n=len(l1)-1
    for i in range(n-1,0,-1):
        exchange=0
        for j in range(i-1):
            if l1[j+1]<l1[j]:
                l1[j+1],l1[j]=l1[j],l1[j+1]
                exchange=1
        if exchange==0:
            break
    return l1



