"""
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
思路：
分割放到列表中
双指针判断首尾是否相等
优化：
直接将数字转换成字符串
直接利用字符串的-index属性来判断
"""
m=12321
l=[]
while m!=0:
    m,y=divmod(m,10)
    l.append(y)
i=0
j=len(l)-1
num=0
while i<j:
    if l[i]==l[j]:
        i+=1
        j-=1
    elif l[i]!=l[j]:
        num=1
        break
if num!=0:
    print('不是回文数')
else:
    print('是回文数')
