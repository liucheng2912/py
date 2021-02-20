'''
思路：
    将正整数变为列表，然后遍历列表，将第一位6转换成9
'''
def maximum69Number(num):
    s=str(num)
    s1=''
    temp=0
    for i in s:
        if i=='9' or temp==1:
            s1+=i
        elif i=='6' and temp==0:
            s1+='9'
            temp=1
    return int(s1)

num = 9669
print(maximum69Number(num))