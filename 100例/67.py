"""
输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
思路：
循环遍历数组，找到最大的元素，与第一个元素交换，
"""
l=[20,10,30,50,100,2,8]
l1=[]
for i in range(len(l)):
    max = l[0]
    for j in range(len(l)):
        if max<l[j]:
            max=l[j]
    l1.append(max)
    l.remove(max)
print(l1)