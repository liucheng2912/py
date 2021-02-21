def jisuan(A):
    for i in range(len(A)):

        A[i]*=A[i]
    return A

A=[-4,-1,0,3,10]
print(jisuan(A))