'''
算法1：将根节点入栈，然后弹出栈顶元素，将值追加到res末尾，然后将右子节点和左子节点一次入栈，因为左子节点要先出栈，所以先入栈右子节点
算法2：cur指向root根节点，将值追加到末尾，将根节点入栈
      然后让cur指向cur.left 继续上述操作
      当cur为None时，弹出根节点，让cur指向cur.right 继续上述操作
算法3：父节点遍历后不入栈，将右子节点入栈
'''


class Solution:
    # 前序遍历
    def pre_order(self, root):
        stack = []
        # 将根节点入栈
        stack.append(root)
        res = []
        while stack:
            # 将栈顶元素弹出，将值存入到res中
            cur = stack.pop()
            res.append(cur.val)
            # 需要先弹出左子节点，所以右子节点先入栈
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res

    def pre_order1(self, root):
        cur = root
        stack = []
        res = []
        while stack or cur:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                cur = cur.right

    def pre_order2(self, root):
        cur = root
        res = []
        stack = []
        while stack or cur:
            if cur:
                res.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()

    def pre_order(self,root):
        if not root:return []
        res=[]
        stack=[root]
        while stack:
            cur=stack.pop()
            if cur.right:
                stack.append(cur.right)
            if cur.right:
                stack.append(cur.left)
        return res

    #标记法迭代，在栈中存放一个标记位
    def pre_order(self,root):
        stack=[(0,root)]
        res=[]
        while stack:
            flag,cur=stack.pop()
            if not cur:continue
            if flag==0:
                stack.append(0,cur.right)
                stack.append(0,cur.left)
                stack.append(1,cur)
            else:
                res.append(cur.val)
        return res









