'''
思路：
    找出每组数里面找最小的数 然后比较 找到最大的数
    再比较有多少组里包含了这个最大的数
思路：
    遍历数组，然后将每组的最小元素存放到字典中，然后找出字典的最大值和数量
'''
def countG(rectangles):
    s={}
    for i in rectangles:
        n = min(i)
        if n not in s:
            s[n]=1
        else:
            s[n]+=1
    max1 = max(s.values())
    return max1

rectangles = [[5,8],[3,9],[5,12],[16,5]]
print(countG(rectangles))
