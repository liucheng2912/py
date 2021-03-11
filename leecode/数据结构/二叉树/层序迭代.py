import collections

from Class1 import TreeNode
class Solution:
    def levelOrder(self,root):
        if not root:return []
        cur=[root]
        res=[]
        while cur:
            lay=[]
            for node in cur:
                res.append(node.val)
                if node.left:lay.append(node.left)
                if node.right:lay.append(node.right)
            cur=lay
        return res

    #标记法
    def levelOrder1(self,root):
        queue=[(0,root)]
        res=[]
        while queue:
            size=len(queue)
            for _ in range(size):
                level=[]
                flag,cur=queue.pop(0)
                if not cur:continue
                if flag==0:
                    queue.append(1,cur)
                    queue.append(0,cur.left)
                    queue.append(0,cur.right)
                else:
                    level.append(cur.val)
            res.append(level)
        return res

    def levelOrder2(self,root):
        queue=collections.deque()
        queue.append(root)
        res=[]
        while queue:
            size=len(queue)
            level=[]
            for _ in range(size):
                cur=queue.popleft()
                if not cur:continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res

    def levelOrder3(self,root):
        queue= collections.deque()
        queue.append(root)
        res=[]
        while queue:
            size=len(queue)
            level=[]
            for _ in range(size):
                cur=queue.popleft()
                if cur:continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res














