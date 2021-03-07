'''
思路：
    顺序查找 比较之后和之前的元素 假如找到比他大的，成功，假如找不到，输出-1
'''
def nextG(nums):
    n=len(nums)
    if n==1:return [-1]
    l=[None]*n
    for i in range(n):
        if i==0:
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    l[i]=nums[j]
                    break
                else:
                    l[i]=-1
        elif i==n-1:
            for j in range(0,i):
                if nums[j]>nums[i]:
                    l[i]=nums[j]
                    break
                else:
                    l[i]=-1
        else:
            temp=0
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    l[i]=nums[j]
                    temp=0
                    break
                else:
                    temp=1
            if temp==1:
                for j in range(0,i):
                    if nums[j]>nums[i]:
                        l[i]=nums[j]
                        break
                    else:
                        l[i]=-1
    return l

nums=[1,5,3,6,8]
print(nextG(nums))
