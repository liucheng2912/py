def get(target):
    l=[]
    for i in range(1,target-1):
        j=i+1
        sum=i+j
        l1=[]
        while sum<target:
            j=j+1
            sum+=j
        if sum==target:
            for m in range(i,j+1):
                l1.append(m)
        if len(l1)>1:
            l.append(l1)
    return l

print(get(15))


