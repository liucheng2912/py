#使用栈来实现
#若是右子节点存在，入栈
#若是左子节点存在，入栈
#最后出栈
def preorder(node):
    stack=[node]
    while len(stack)>0:
        print(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
        stack.pop()

def midorder(node):
    stack=[]
    pos=node
    while pos is not None or len(stack)>0:
        if pos is not None:
            stack.append(pos)
            pos=pos.left
        else:
            pos=stack.pop()
            print(pos.val)
            pos=pos.right


