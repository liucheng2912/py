'''
思路：
    将整数转换成字符串，比较len长度
'''
def f(nums):
    temp=0
    for i in nums:
        if len(str(i))%2==0:
            temp+=1
    return temp

nums = [555,901,482,1771]
print(f(nums))