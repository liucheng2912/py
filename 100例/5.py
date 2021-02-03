"""
输入三个整数x,y,z，请把这三个数由小到大输出。
思路：
1、输入
2、排序
直接比较
3、输出
缺点：
输入时没有考虑到在循环语句中直接输入
sort了之后直接输出列表即可
"""

a=[]
for i in range(3):
    x = int(input('请输入:'))
    a.append(x)

a.sort()
print(a)