#前后同时移动判断是否相等
x = 0
x =str(x)
i=0
j=len(x)-1
while i<j:
    temp = 0
    len1=len(x)//2
    if x[i]==x[j]:
        i=i+1
        j=j-1
        temp =1
    else:
        print("false")
        break
print("true")





