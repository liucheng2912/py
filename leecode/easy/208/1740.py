'''
思路：
字符串截断，然后遍历字符串，判断字符含有的元音数目是否相等
'''
def f(s):
    s1=s[:len(s)//2]
    s2=s[len(s)//2:]
    temp1=0
    temp2=0
    n=['a','e','i','o','u','A','E','I','O','U']
    for i in n:
        temp1+=s1.count(i)
        temp2+=s2.count(i)
    if temp1==temp2:
        return True
    else:
        return False

s = "MerryChristmas"
print(f(s))