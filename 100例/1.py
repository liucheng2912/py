"""
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
思路：个十百分别依次填入
百位有4种填法 十位有3种填法  个位有2种填法
3次遍历，只要三个数不相等，就可以进行输出
伪代码：
for i in range(1,5):
    百位 i1=i*100
        for j in range(1,5):
            if i==j:
                break
            else:
                十位 j1=j*10
            for n in range(1,5):
                if n==i or n==j:
                    break
                else:
                    个位 n1=n
    result = i1+j1+n1
"""
for i in range(1,5):
    for j in range(1,5):
        for n in range(1,5):
            if (i!=j) and (i!=n) and (j!=n):
                print(i*100+j*10+n)
