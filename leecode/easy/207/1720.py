"""
思路：
a^b=c a^c=b
首先将first放入列表中
e[0]=a[0]^a[1]  a[0]=1 a[1]=a[0]^e[0]
e[1]=a[1]^a[2]  a[2]=a[1]^e[1]
"""
def f(encoded,first):
    l=[]
    l.append(first)
    for i in range(len(encoded)):
        temp=encoded[i]^l[i]
        l.append(temp)
    return l

encoded = [6,2,7,3]
first = 4
print(f(encoded, first))