"""
有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中
思路：插入排序
遍历数组，找到小于的那个元素，将其插入
特殊点 末尾追加的效果
l.insert(n,s)
"""
l=[1,3,5,7,10]
s=1
count=0
for i in range(len(l)):
    if s<l[i]:
       l.insert(i,s)
       count=1
    if count==1:
        break
if count!=1:
    l.append(s)
print(l)