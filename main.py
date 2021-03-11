import collections

from Class1 import ListNode
class Solution:
    def levelOrder(self,root):
        queue=[root]
        res=[]
        while queue:
            size=len(queue)
            level=[]
            for _ in range(size):
                cur=queue.pop(0)
                if not cur:continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res

