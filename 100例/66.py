"""
输入3个数a,b,c，按大小顺序输出
"""
l=[]
for i in range(3):
    a = int(input('请输入：'))
    l.append(a)
l.sort()
print(l)