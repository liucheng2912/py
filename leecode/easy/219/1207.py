'''
思路：
    利用字典
'''
def uniqueOccurrences(arr):
    s={}
    for i in arr:
        if i not in s:
            s[i]=1
        else:
            s[i]+=1
    l=set()
    for i in s:
        if s[i] not in l:
            l.add(s[i])
        else:
            return False
    return True

arr = [1,2,2,1,1,3]
print(uniqueOccurrences(arr))