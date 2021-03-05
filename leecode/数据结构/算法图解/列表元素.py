def find_num(l):
    total=0
    if len(l)==1:total=1
    else:
        total+=1+find_num(l[1:])
    return total

l=[1,2,3]
print(find_num(l))
