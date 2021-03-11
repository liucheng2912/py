from Class1 import TreeNode
class Solution:
    def inorderTravelsal(self,root):
        cur=root
        res=[]
        stack=[]
        while stack or cur:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.poo()
            res.append(cur.val)
            cur=cur.right
        return res