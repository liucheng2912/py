'''
思路：
    1:将两个列表排序，然后遍历比较是否相等
    2:遍历列表target，将其存放到字典，然后遍历arr，判断arr是否在字典中，并比较出现次数
'''
def canBeEqual(target,arr):
    s={}
    for i in range(len(target)):
        if target[i] not in s:
            s[target[i]]=1
        else:
            s[target[i]] += 1
        if arr[i] not in s:
            s[arr[i]]=-1
        else:
            s[arr[i]]-=1
    for i in s:
        if s[i]!=0:
            return False
    return True



target = [1,2,3,4]
arr = [2,5,1,3]
print(canBeEqual(target, arr))