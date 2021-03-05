"""
结束条件
假如l1为空，返回l2
假如l2为空，返回l1
循环条件
取两个列表头部中较小的那个，然后再加上合并其余元素得到的结果
if l1.val<l2.val:
    l1.next=f(l1.next,l2)
    return l1
else:
    l2.next=f(l1,l2.next)
    return l2

"""

from Class1 import ListNode

class Solution(object):
    def merge1(self,l1:ListNode,l2:ListNode):
        if not l1:return l2
        if not l2:return l1
        if l1.val<l2.val:
            l1.next = self.merge1(l1.next,l2)
            return l1
        else:
            l2.next = self.merge1(l1,l2.next)
            return l2