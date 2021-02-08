'''
思路：
    遍历整数数组，拿到值作为s的下标，然后相加
'''
def f(s,indices):
    s1=[None]*len(s)
    for i in range(len(indices)):
        s1[indices[i]]=s[i]
    return ''.join(s1)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(f(s, indices))
