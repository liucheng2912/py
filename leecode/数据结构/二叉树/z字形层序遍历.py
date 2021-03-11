import collections

from Class1 import TreeNode
class Solution:
    def ziglevelOrder(self,root):
        queue=collections.deque()
        queue.append(root)
        res=[]
        is_Even_level=True
        while queue:
            size=len(queue)
            level=collections.deque()
            for _ in range(size):
                cur=queue.popleft()
                if is_Even_level:
                    level.append(cur.val)
                else:
                    level.appendleft(cur.val)
                if queue.left:queue.append(cur.left)
                if queue.right:queue.append(cur.right)
            res.append(list(level))
            is_Even_level= not is_Even_level
        return res
