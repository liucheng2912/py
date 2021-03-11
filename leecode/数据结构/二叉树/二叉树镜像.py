'''
思路：
    左右子树交换
    利用栈
'''
from Class1 import TreeNode
class Solution:
    def mirrorTree(self,root):
        if not root:return
        stack=[root]
        while stack:
            node=stack.pop()
            if node.left:stack.append(node.left)
            if node.right:stack.append(node.right)
            node.left,node.right=node.right,node.left
        return root

