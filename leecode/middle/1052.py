'''
思路：
    首先计算老板不生气时满意的客户，然后计算滑动窗口内因为改变态度而挽留的客人
'''
def maxs(customers,grumpy,X):
    temp=0
    for i in range(len(customers)):
        if grumpy[i]==0:
            temp+=customers[i]

    temp1=0
    for i in range(X):
        if grumpy[i]==1:
            temp1+=customers[i]

    temp2=temp1
    for j in range(X,len(customers)):
        if grumpy[j]==1:
            temp2+=customers[j]
        if grumpy[j-X]==1:
            temp2-=customers[j-X]

        temp1=max(temp1,temp2)

    return temp+temp1

customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 3
print(maxs(customers, grumpy, X))

