'''
思路：
    cur初始化root
    cur!=None 说明还有左子节点在，将cur入栈，并且将cur置为他的左子节点
    cur为None时，说明到二叉树左下节点了，栈顶父节点出栈赋值给cur，并保存节点值到list
    将cur置为栈顶节点的右子节点继续循环

'''
from Class1 import TreeNode
class Solution:
    def in_order(self,root):
        cur=root
        stack=[]
        res=[]
        #栈非空或cur非None时，循环
        while stack or cur:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                cur=stack.pop()
                res.append(cur.val)
                cur=cur.right
        return res

    def in_order(self,root):
        stack=[(0,root)]
        res=[]
        while stack:
            flag,cur=stack.pop()
            if not cur:continue
            if flag==0:
                stack.append(0,cur.right)
                stack.append(1,cur)
                stack.append(0,cur.left)
            else:
                res.append(cur.val)
        return res
























