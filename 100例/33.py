"""
按逗号分隔列表。
思路：
join , 将列表元素转换成string类型
缺点：
join的用法 一串字符串中每个和前面的内容相加
列表表达式
"""
m=''
l1=[1,2,3,4,5]
m+=','.join(str(i) for i in l1)
print(m)