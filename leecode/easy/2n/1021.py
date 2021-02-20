'''
思路：
    栈
'''
def removeOuter(S):
    l1=[]
    l2=''
    for i in S:
        if i=='(':
            if l1:l2+=i
            l1.append(i)
        if i==')':
            l1.pop()
            if l1:l2+=i
    return l2

s="(()())(())(()(()))"
print(removeOuter(s))