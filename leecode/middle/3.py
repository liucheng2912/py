'''
思路：
    滑动窗口
'''
def le(s):
    occ=set()
    ans=0
    rk=-1
    for i in range(len(s)):
        while i!=0:
            occ.remove(s[i-1])
        while rk<len(s) and rk[i+1] not in occ:
            occ.add(s[rk+1])
            rk+=1
        ans = max(ans,rk-i+1)
    return ans

s = "dvdf"
print(le(s))
