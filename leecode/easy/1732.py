'''
思路：
    gain[i] 是点i和点i+1的高度差
    num[i+1]=gain[i]+nums[i]
'''
def f(gain):
    l=[]
    l.append(0)
    for i in range(len(gain)):
        l.append(l[i]+gain[i])
    return max(l)

gain = [-4,-3,-2,-1,4,3,2]
print(f(gain))
