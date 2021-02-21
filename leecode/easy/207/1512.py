'''
思路：
1、遍历数组
'''
def f(n):
    temp=0
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[i] == n[j]:
                temp += 1
    return temp

nums = [1,1,1,1]
print(f(nums))
print(f1(nums))