'''
思路：
    通过set转换，比较长度是否相等
'''
def f(s):
    s1=set(s)
    return len(s1)==len(s)