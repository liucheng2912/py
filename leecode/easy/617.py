'''
思路：
    定义一个新的二叉树，然后遍历这两个二叉树
'''

from Class1 import TreeNode

class Solution:
    def mergeTree(self,root1,root2):
        if not root1 or not root2:
            return root1 or root2
        root1.val = root1.val+root2.val
        root1.left = self.mergeTree(root1.left,root2.left)
        root1.right=self.mergeTree(root1.right,root2.right)
        return root1
