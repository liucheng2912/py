"""
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
思路：
几位数 //10 和 %10 divmod
将列表依次输出
"""
n=int(input())
l=[]
while n!=0:
    n,y=divmod(n,10)
    l.append(y)

for i in l:
    print(i)
