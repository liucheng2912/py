"""
思路：
新建一个数组，假如他的index是偶数位，增加前n的数组
假如index是奇数位，增加后n的数组
"""
def f(nums,n):
    l=[]
    x=0
    y=n
    for i in range(2*n):
        if i%2==0:
            l.append(nums[x])
            x+=1
        else:
            l.append(nums[y])
            y+=1
    return l
nums = [1,2,3,4,4,3,2,1]
n = 4
print(f(nums, n))
