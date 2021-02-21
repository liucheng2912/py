'''
思路：
字典存放 比较四个值是否相等
'''
def f(moves):
    d={}
    for i in moves:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    if len(d)==2:
        if d.setdefault('L')==d.setdefault('R') or d.setdefault('U')==d.setdefault('D'):
            return True
    elif len(d)==4:
        if d.setdefault('L')==d.setdefault('R') and d.setdefault('U')==d.setdefault('D'):
            return True
    return False

s="UD"
print(f(s))
s="LL"
print(f(s))

