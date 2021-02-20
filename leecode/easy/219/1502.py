'''
思路：
    通过最小的两个值，确定这个差值，然后依次相加这个差值，判断数值是否在列表中
    若是在，则继续相加
    若是不在，则返回false
'''
def canMakeArithmeticProgession(arr):
    temp1=min(arr)
    arr.pop(arr.index(temp1))
    temp2=min(arr)
    arr.pop(arr.index(temp2))
    temp3=temp2-temp1
    temp4=temp2+temp3
    while len(arr)>0:
        if temp4 in arr:
            arr.pop(arr.index(temp4))
        else:
            return False
        temp4 += temp3
    return True

arr = [1,2,4]
print(canMakeArithmeticProgession(arr))
