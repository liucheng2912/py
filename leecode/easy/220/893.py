'''
思路：
    题意分析：偶数位只能和偶数位交换，奇数位只能和奇数位交换
    可以通过判断偶数位元素是否相等，奇数位元素是否相等来判断是否可通过交换实现
    遍历字符串
    将偶数位元素和奇数位元素进行比较
    然后记录所有的对数
    使用列表还存储存储每个元素出现的次数
'''
def numSpecicalEquivFroups(A):
    s=set()
    for i in A:
        s.add(''.join(sorted(i[::2]))+''.join(sorted(i[1::2])))
    return len(s)

s=["abc","acb","bac","bca","cab","cba"]
print(numSpecicalEquivFroups(s))




