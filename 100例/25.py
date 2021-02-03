"""
求1+2!+3!+...+20!的和。
思路：
reduce
遍历 n!=n*(n-1)*...1
缺点：
缺少了20的值
"""
from functools import reduce

l=[]
l.append(1)
for i in range(2,21):
    num=1
    for j in range(i,0,-1):
        num*=j
    l.append(num)

sum = reduce(lambda x,y:x+y,l)
print(sum)