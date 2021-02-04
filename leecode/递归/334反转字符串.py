"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
输入：["h","e","l","l","o"]
思路：
递归
结束条件 i和j相等
循环条件 交换
"""
def f(l):
    if len(l)<=1:
        return l
    i = 0
    j = len(l)-1
    while i<j:
        l[i],l[j]=l[j],l[i]
        i+=1
        j-=1
    return l

l=["H","a","n","n","a","h"]
print(f(l))