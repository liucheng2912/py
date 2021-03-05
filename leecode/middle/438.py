'''
思路：
left right指针
移动指针的时候 假如使用了k，则加回去，判断
'''
import collections


def f(s,k):
    counter =collections.Counter()
    left,right,res=0,1,0
    while right<len(s):
        counter[s[right]]+=1
        while right-left+1-counter.most_common(1)[0][1]>k:
            counter[s[left]]-=1
            left+=1
        res = max(res,right-left+1)
        right+=1
    return res

s = "AABABBA"
k = 1
print(f(s, k))


