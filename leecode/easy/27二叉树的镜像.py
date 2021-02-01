# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        '''递归方法，递归镜像左子节点和右子节点，结束条件是节点为根节点 O(n)'''
        if not root:
            return None
        else:
            root.left,root.right=self.mirrorTree(root.right),self.mirrorTree(root.left)
            return root
        #迭代法 每个子节点左右子树交换，然后组合O(n)
        if not root:return None
        #将二叉树中的节点逐层放入队列中，再迭代处理队列中的元素
        stack=[root]
        while stack:
            #每次从队列中拿一个节点，并交换这个节点的左右字数
            node=stack.pop(0)
            node.left, node.right = node.right, node.left
            #若当前节点的左子树不为空，放入队列等待后续处理
            if node.left:stack.append(node.left)
            # 若当前节点的右子树不为空，放入队列等待后续处理
            if node.right:stack.append(node.right)
        #返回处理完的根节点
        return root




