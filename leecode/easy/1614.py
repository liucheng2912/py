'''
思路：
    遍历，遇到(则加1，遇到)则减一，返回最大值
'''
def f(s):
    maxnum=num=0
    for i in s:
        if i =='(':
            num+=1
            maxnum = max(maxnum,num)
        elif i==')':
            num-=1
    return maxnum

s = "(1)+((2))+(((3)))"
print(f(s))
