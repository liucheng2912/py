def get1(n,target):
    l1=list(n)
    l2=[]
    i,j=0,k
    while j<len(l1):
        l2.append(l1[j])
        j+=1
    while i<k:
        l2.append(l1[i])
        i+=1
    return ''.join(l2)



s = "abcdefg"
k = 2
print(get1(s,k))
