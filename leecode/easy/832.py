'''
思路：
    翻转，然后替换
'''
def f(A):
    for i in A:
        for j in range(len(A)):
            if i[j]==0:i[j]=1
            else:i[j]=0
        i.reverse()
    return A

A=[[1,1,0],[1,0,1],[0,0,0]]
print(f(A))