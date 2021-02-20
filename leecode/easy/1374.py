'''
思路：
    n次
    判断n是奇数还是偶数
    若是偶数，则用两个字符
    若是奇数，则用一个字符
'''
def generateTheString(n):
    s=''
    if n%2==0:
        for i in range(n-1):
            s+='a'
        s+='b'
    else:
        for i in range(n):
            s+='a'
    return s

n=3
print(generateTheString(n))