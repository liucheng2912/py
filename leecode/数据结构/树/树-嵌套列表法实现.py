#用数组实现，每个节点都是三元数组
#定义树
def BinaryTree(r):
    return [r,[],[]]

#插入左子树
def inserLeft(r,newBranch):
    #取出r的左子树
    i = r.pop(1)
    #若左子树存在
    if len(i)>1:
        r.insert(1,[newBranch,i,[]])
    else:
        r.insert(1,[newBranch,[],[]])

#插入右子树
def insertRight(r,newBranch):
    i = r.pop(2)
    if len(i)>1:
        r.insert(2,[newBranch,[],i])
    else:
        r.insert(2,[newBranch,[],[]])

#获取根值
def getRootVal(r):
    return r[0]

#根赋值
def setRootVal(r,val):
    r[0]=val

#取左子树
def getLeftChild(r):
    return r[1]

#取右子树
def getRightChild(r):
    return r[2]

if __name__=='__main__':
    r=BinaryTree(3)
    inserLeft(r,4)
    inserLeft(r,5)
    insertRight(r,6)
    insertRight(r,7)
    l=getLeftChild(r)
    print(l)
    setRootVal(l,9)
    print(r)
    inserLeft(l,11)
    print(r)
    print(getRightChild(getRightChild(r)))