'''
添加一个high 标记层数，奇数层从左往右，偶数层从右往左
'''
from Class1 import ListNode
class Soultion:
    def zigzagLevelOrder(self,root):
        queue=[root]
        res=[]
        high=0
        while queue:
            size=len(queue)
            level=[]
            for _ in range(size):
                cur=queue.pop(0)
                if high%2==0:
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    queue.append(cur.right)
                    queue.append(cur.left)
                level.append(cur.val)
            if level:
                res.append(level)
            high+=1
        return res

