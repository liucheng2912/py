'''
思路：
    栈 先入先出，一个L对应一个R
'''
def balancedStringSplit(s):
    l=[]
    count=0
    for i in s:
        if len(l)==0:
                l.append(i)
        else:
            if i not in l:
                l.pop()
                if len(l)==0:
                    count+=1
            else:
                l.append(i)
    return count

s = "RLRRRLLRLL"
print(balancedStringSplit(s))