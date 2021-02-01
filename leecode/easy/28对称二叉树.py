'''
递归的方法实现
当左右子树都为none的时候，这个root为对称的
当一边为空或者左右子树的val不相等时，不是对称的
然后对左右子树进行递归调用，判断是否是对称的
'''
def order(l1):
    def order1(l1,l2):
        if not l1 and not l2:
            return True
        elif not l1 or not l2 or l1.val!=l2.val:
            return False
        return order1(l1.left,l2.right) and order1(l1.right,l2.left)
    return order1(l1.left,l1.left)