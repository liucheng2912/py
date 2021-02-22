'''
思路:
    找出中值
    然后遍历填充树
    将left和right依次填入一个新列表

'''

from Class1 import TreeNode

class Solution:
    def sortA(self,nums):
        def makeTree(start_index,end_index):
            if start_index>end_index:
                return None
            mid=(end_index+start_index)//2
            tree = TreeNode(nums[mid])
            tree.left = makeTree(start_index,mid-1)
            tree.right=makeTree(mid+1,end_index)
            return tree

        return makeTree(0,len(nums)-1) if nums else None
