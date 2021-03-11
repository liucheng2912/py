'''
对应前序的反操作
将root.valres插入到第一位
'''


class Solution:
    def in_order(self, root):
        cur = root
        stack = []
        res = []
        while cur and stack:
            if cur:
                # 将root.val插入到第一位，每次都插入到第一位，相当于从头部追加
                res.insert(0, cur.val)
                # 将根节点入栈
                stack.append(cur)
                # 然后指向右子节点，将右子节点做头部追加
                cur = cur.right
            else:
                # 右子节点为空，根节点弹出，指向左子节点，然后从头部追加
                cur = stack.pop()
                cur = cur.left
        return res


    def post_order(self,root):
        res=[]
        stack=[root]
        while stack:
            cur=stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return res[::-1]

    #标记位
    def post_order1(self,root):
        stack=[(0,root)]
        res=[]
        while stack:
            flag,cur=stack.pop()
            if not cur:continue
            if flag==0:
                stack.append(1,cur)
                stack.append(0,cur.right)
                stack.append(0,cur.left)
            else:
                res.append(cur.val)
        return res

