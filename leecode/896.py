'''
思路：
    判断前两个字符的大小
    然后判断后续元素是否也是同样排序
'''
def f(A):
    s=[A[0]]+A+[A[-1]]
    temp1=0
    temp2=0
    for i in range(1,len(s)-1):
        if s[i]>=s[i-1] and s[i]<=s[i+1]:
            temp1+=1
    for i in range(1, len(s) - 1):
        if s[i]<=s[i-1] and s[i]>=s[i+1]:
            temp2+=1
    if temp1==len(s)-2 or temp2==len(s)-2:
        return True
    return False

A=[6,5,4,4]
print(f(A))