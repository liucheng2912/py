import math
n=[1,1,2,4,5,10,12]
sum=0
temp=0
for i in range(len(n)-2):
    sum=abs(n[i+1]-n[i])
    if temp<sum:
        temp=sum

print(temp)
