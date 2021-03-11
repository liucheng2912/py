'''
思路：
寻找子节点的公共祖先 即 寻找子节点的父节点的公共祖先
用栈来存放 从根节点到子节点的内容，然后栈顶元素弹出，第一个相同的元素
则为祖先节点
'''
from Class1 import ListNode
class Solution:
    def lowestCommonAncestor(self,root,p,q):
        stack1=self.find(root,p)
        stack2=self.find(root,q)
        while stack1 and stack2:
            c1=stack1.pop()
            c2=stack2.pop()
            if c1.val==c2.val:
                return c1.val


    def find(self,root,x):
        stack=[]
        cur=root
        while stack or cur:
            while cur:
                if cur.val!=x:
                    stack.append(cur)
                    cur=cur.left
                else:
                    break
            cur=stack.pop()
            if cur.val!=x:
                cur=cur.right
            else:
                break
        return stack



