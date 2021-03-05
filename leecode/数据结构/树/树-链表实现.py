class BinaryTree:
    #初始化一个node
    def __init__(self,RootVal):
        self.key=RootVal
        self.leftchild=None
        self.rightchild=None

    #插入左子树
    def insertLeft(self,newnode):
        #左子树为空时，直接插入
        if self.leftchild==None:
            self.leftchild=BinaryTree(newnode)
        #左子树不为空的时候，先将新节点的左子树指向现在的左子树，再将根节点的左子树指向现在的新节点
        else:
            p=BinaryTree(newnode)
            p.leftchild=self.leftchild
            self.leftchild=p

    def insertRight(self,newnode):
        if self.rightchild==None:
            self.rightchild=BinaryTree(newnode)
        else:
            p=BinaryTree(newnode)
            p.rightchild=self.rightchild
            self.rightchild=p

    def getRootVal(self):
        return self.key

    def getLeftChild(self):
        return self.leftchild

    def getRightChild(self):
        return self.rightchild

    def setRootVal(self,Rootval):
        self.key=Rootval

if __name__=='__main__':
    r=BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')
    r.getRightChild().setRootVal('hello')
    r.getLeftChild().insertRight('d')
    print(r)