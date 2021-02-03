"""
打印杨辉三角
思路：
第n行为第n-1行的两两相加之和，再在首尾加上1
"""
tr=[[1],[1,1]]
n=10
for i in range(2,n):
    l=[1]
    pre=tr[i-1]
    for j in range(i-1):
        l.append(pre[j]+pre[j+1])
    l.append(1)
    tr.append(l)

for i in tr:
    print(i)




