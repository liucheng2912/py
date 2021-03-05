'''
思路：
    将字符串word2进行分割，切取多余的部分
    然后将word1和word2分别添加进一个数组的偶数位去
'''
def f(word1,word2):
    n1=len(word1)
    n2=len(word2)
    n=min(n1,n2)
    l=[]
    x=0
    y=0
    for i in range(n*2):
        if i%2==0:
            l.append(word1[x])
            x+=1
        else:
            l.append(word2[y])
            y+=1
    if n1>n2:
        l.append(word1[n2:])
    if n2>n1:
        l.append(word2[n1:])
    if n1==n2==0:
        return ''
    return ''.join(l)


word1 = ""
word2 = ""
print(f(word1, word2))