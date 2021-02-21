def get1(l):
    l1=[]
    l1=l.split(" ")
    p1,p2=0,len(l1)-1
    while p1<=p2:
        l1[p1],l1[p2]=l1[p2],l1[p1]
        p1+=1
        p2-=1

    return ' '.join(l1)






s1="a good   example"
print(get1(s1))