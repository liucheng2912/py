'''
层序遍历
'''
from collections import deque


class Solution:
    def maxDepth(self,root):
        if not root:return 0
        queue=deque()
        queue.append(root)
        res=0
        while queue:
            tmp=[]
            for node in queue:
                if node.left:tmp.append(node.left)
                if node.right:tmp.append(node.right)
            queue=tmp
            res+=1
        return res

