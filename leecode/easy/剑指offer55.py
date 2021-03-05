'''
思路：
    最大深度为左子树最大深度和右子树最大深度的最大值+1
'''
from Class1 import TreeNode
class Solution:
    def maxDepth(self,root):
        if not root:return
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

