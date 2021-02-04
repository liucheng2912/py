# Definition for singly-linked list.
#链表合并
#思路：合并链表l1和l2 等于合并l1.next和l2orl1和l2.next 结束条件l2.next为null or l1.next为null
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode):
        if not l1:return l2
        if not l2:return l1
        if l1.val<=l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
