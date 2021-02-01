
class Tree():
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
#前序遍历
def preorder(tree):
    if tree==None:
        return False
    print(tree)
    preorder(tree.leftchild)
    preorder(tree.rightchild)
#中序遍历
def midorder(tree):
    if tree==None:
        return False
    midorder(tree.leftchild)
    print(tree)
    midorder(tree.rightchild)
#后序遍历
def backorder(tree):
    if tree==None:
        return False
    backorder(tree.leftchild)
    backorder(tree.rightchild)
    print(tree)

