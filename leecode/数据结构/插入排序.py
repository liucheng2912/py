'''[49,38,65,97,76,13,27,49]
i=0 49
i=1>0 38<49 交换位置 [38,49]
i=2>0 65>49 [38,49,65]
i=3>0 97>65 [38,49,65,97]
i=4>0 76<97 交换位置[38,49,65,76,97] i-1 3 76>65 不变
i=5》0 13<97 交换位置[38,49,65,76,13,97] i-1=4 13<76 交换位置 i-1.。。。
时间复杂度O(n^2)
'''
def order5(l1):
    for i in range(len(l1)):
        while i>0 and l1[i]<l1[i-1]:#小于前一个值的时候交换位置
            l1[i],l1[i-1]=l1[i-1],l1[i]
            i-=1
    return  l1

print(order5([22,21,12,44,21]))






