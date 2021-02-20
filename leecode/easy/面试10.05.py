'''
思路：
    二分查找，
    假如找到的是非空字符串，判断大小，然后继续查找
    假如找到的是空字符串，就记住位置
    然后向前移动，直到找到非空的字符串
    假如小于s，则用空字符串的位置加1再进行查找
    假如大于s，则用非空字符串所在的位置替换
'''
def findString(words,s):
    left,right=0,len(words)-1
    while left<=right:
        mid=(left+right)//2
        temp=mid
        while words[mid]=='' and mid<right:
            mid+=1
        if words[mid]=='':
            right =temp-1
            continue
        if words[mid]==s:
            return mid
        elif s<words[mid]:
            right=mid-1
        else:
            left=mid+1
    return -1

words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""]
s = "ta"
print(findString(words, s))
words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""]
s = "ball"
print(findString(words, s))

