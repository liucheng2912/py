'''
思路：
    遍历数组，将元素和出现次数存在字典中
    将字典中元素只出现一次的元素进行求和
'''
def f(nums):
    a={}
    sum=0
    for i in nums:
        if i not in a:
            a[i]=1
        else:
            a[i]+=1
    for i in a:
        if a[i]==1:
            sum+=i
    return sum

nums=[1,2,3,2]
print(f(nums))