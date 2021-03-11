'''
思路：
    层序遍历两个树
'''
from collections import deque

from Class1 import ListNode, TreeNode


class Solution:
    def mergeTrees(self,root1,root2):
        if not root1:return root2
        if not root2:return root1
        merged=TreeNode(root1.val+root2.val)
        queue1=deque([root1])
        queue2=deque([root2])
        queue=deque([merged])
        while queue1 and queue2:
            cur=queue.popleft()
            cur1=queue1.popleft()
            cur2=queue2.popleft()
            l1,r1=cur1.left,cur1.right
            l2,r2=cur2.left,cur2.right
            if l1 or l2:
                if l1 and l2:
                    l=TreeNode(l1.val+l2.val)
                    cur.left=l
                    queue.append(l)
                    queue1.append(l1)
                    queue2.append(l2)
                elif l1:
                    cur.left=l1
                elif l2:
                    cur.left=l2
            if r1 or r2:
                if r1 and r2:
                    r=TreeNode(r1.val+r2.val)
                    cur.right=r
                    queue.append(r)
                    queue1.append(r1)
                    queue2.append(r2)
                elif l1:
                    cur.left=l1
                elif l2:
                    cur.left=l2
        return merged



