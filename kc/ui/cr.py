
def order(l1):
    for i in range(len(l1)):
        while i>0 and l1[i]<l1[i-1]:
            l1[i],l1[i-1]=l1[i-1],l1[i]
            i=i-1
    return l1

print(order([22,21,12,44,21]))