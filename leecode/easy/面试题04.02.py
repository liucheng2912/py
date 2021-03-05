'''
思路：
    每次取中值
    然后对小于中值的继续进行操作
    对大于中值的继续进行操作
    返回每次的中值
'''
from Class1 import TreeNode

def sortA(nums):
    if not nums:
        return
    tree = TreeNode(nums[len(nums)//2])
    tree.left=sortA(nums[:len(nums)//2])
    tree.right=sortA(nums[len(nums)//2+1:])
    return tree



