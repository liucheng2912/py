#递归
from Class1 import TreeNode
class Solution:
    def threeOrders(self,root):
        pre_order=[]
        in_order=[]
        post_order=[]
        #前序遍历
        def pre_find(root):
            if not root: return None
            pre_order.append(root.val)
            pre_find(root.left)
            pre_find(root.right)
        #中序遍历
        def in_find(root):
            if not root:return None
            in_find(root.left)
            in_order.append(root.val)
            in_find(root.right)

        #后续遍历
        def post_find(root):
            if not root:return None
            post_find(root.left)
            post_find(root.right)
            post_order.append(root.val)

        pre_find(root)
        in_find(root)
        post_find(root)
        return [pre_order,in_order,post_order]


