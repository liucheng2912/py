'''
思路：
    在上边界和下边界中循环计算
    将整数对10进行除法运算，假如商为0，则除尽
    为了减少重复运算，利用一个字典存放是否是自除数
'''
def selfDivdingNumbers(left:int,right:int):
    l=[]
    for i in range(left,right+1):
        n = i
        temp1=0
        if i<10:
            l.append(i)
        else:
            while n>9:
                temp=n%10
                if temp==0:
                    temp1=-1
                    break
                result = i % temp
                n = n // 10
                if result != 0:
                    temp1 = -1
                    break
            else:
               if i%n!=0:
                   temp1=-1
            if temp1!=-1:
                    l.append(i)
    return l
left=1
right=22
print(selfDivdingNumbers(left, right))

