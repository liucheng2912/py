'''
思路：
    遍历字符串，判断每个字符是否是都在allowed中
'''
def f(allowed,words):
    temp=0
    for i in words:
        temp1 = 0
        for j in i:
            if j not in allowed:
                temp1=1
                break
        if temp1==0:
            temp+=1
    return temp

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
print(f(allowed, words))

