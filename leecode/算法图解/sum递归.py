def sum1(l):
    total=0
    if len(l)==1:total=l[0]
    else:
        total+=l[0]+sum1(l[1:])
    return total

l=[1,2,3]
print(sum(l))