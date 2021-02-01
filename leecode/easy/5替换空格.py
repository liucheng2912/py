def replaceSpace(l1):
    for i in range(len(l1)):
        l2=list(l1)
        for i in range(len(l2)):
            if l2[i]==' ':
                l2[i]='%20'
            else:
                l2[i]=l1[i]
            i+=1
    return ''.join(l2)

a=replaceSpace("We are happy")
print(a)