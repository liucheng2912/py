'''
思路：
    遍历字符串，然后计算得到x和y的结果
'''

def f(s):
    x=1
    y=0
    for i in s:
        if i=='A':
            x=2*x+y
        elif i=='B':
            y=2*y+x
    return x+y

s='ABAB'
print(f(s))
