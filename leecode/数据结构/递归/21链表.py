# Definition for singly-linked list.
#链表合并
#思路：合并链表l1和l2 等于合并l1.next和l2 or l1和l2.next 结束条件l2.next为null or l1.next为null
#取两个列表头部中较小的那个，然后再加上合并其余元素所得到的的结果
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode):
        if l1 is None:return l2
        elif l2 is None:return l1
        elif l1.val<=l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2