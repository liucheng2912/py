def ham(n:int):
    #直接用bin函数，将n转换成二进制，然后数1
    #print(type(bin(n)))
    #return bin(n).count('1')

    #转换成二进制，再利用字典
    k=format(n,'b')
    #print(type(k))
    d={'0':0,'1':0}
    for i in k:
        if i in d:
            d[i]+=1
    return d['1']

n=9
print(ham(n))
