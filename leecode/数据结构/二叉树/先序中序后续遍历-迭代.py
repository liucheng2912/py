from Class1 import TreeNode
class Solution:
    def threeOrder(self,root):
        pre_order,in_order,post_order=[],[],[]
        def pre_find(root):
            cur=root
            stack=[]
            while cur or stack:
                if cur:
                    post_order.append(cur.val)
                    stack.append(cur)
                    cur=cur.left
                else:
                    cur=stack.pop()
                    cur=cur.right
        def in_find(root):
            cur=root
            stack=[]
            while stack or cur:
                if cur:
                    stack.append(cur)
                    cur=cur.left
                else:
                    cur=stack.pop()
                    in_order.append(cur.val)
                    cur=cur.right
        def post_find(root):
            cur=root
            stack=[]
            while stack or cur:
                if cur:
                    post_order.insert(0,cur.val)
                    stack.append(cur)
                    cur=cur.right
                else:
                    cur=stack.pop()
                    cur=cur.left

