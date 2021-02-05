"""
思路：
字符串不是可变的，首先将字符串转换成列表
替换
特殊情况
1、位于第一位，比较下一位的字符
2、位于最后一位，比较前一位的字符
3、位于中间，比较前后的字符
从一个存放 26个 字母中取出一个
"""
def f(s):
    a='abcdefghijklmnopqrst'
    l=[]
    if len(s)==1:
        return a[0]
    for i in s:
        l.append(i)
    for j in range(len(l)):
        if l[j]=='?':
            if j==0:
                for i in range(0, 26):
                    if l[j+1] != a[i]:
                        l[j]=a[i]
                        break
            elif j==len(l)-1:
                for i in range(0, 26):
                    if l[j-1] != a[i]:
                        l[j]=a[i]
                        break
            else:
                for i in range(0, 26):
                    if l[j-1] != a[i] and l[j+1] != a[i]:
                        l[j]=a[i]
                        break
    b=''
    for i in l:
        b+=i
    return b

s = "??yw?ipkj?"
print(f(s))