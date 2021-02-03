'''
打印对称菱形，需要有居中显示 1 3 5 7 5 3 1
思路：
菱形打印 分成两段打印
空格增加
i=0 k=3 j=1---*
i=1 k=2 j=3--***
i=2 k=1 j=5-*****
i=3 k=0 j=7******
k=3-i j=2i+1
i=4 0 k=1 j=5-*****
i=5 1 k=2 j=3--***
i=6 2 k=3 j=1---*
k=i+1 j=5-2*i
'''
n=7
for i in range(4):
    str=''
    k=3-i
    for x in range(k):
        str+=' '
    j=2*i+1
    for y in range(j):
        str+='*'
    print(str)

for i in range(0,3):
    str=''
    k=i+1
    j=5-2*i
    for x in range(k):
        str+=' '
    for y in range(j):
        str+='*'
    print(str)




