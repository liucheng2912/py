'''
思路：
遍历J 然后遍历S
temp++
也可以直接用s.count
'''
def f(j,s):
    temp=0
    for n in j:
        for m in s:
            if n==m:
                temp+=1
    return temp

def f1(j,s):
    temp=0
    for i in j:
        temp+=s.count(j)
    return temp

J = "z"
S = "ZZ"
print(f(J, S))
print(f1(J, S))