"""
给定链表，交换每两个相邻节点并返回其头节点。

例如，对于列表1-> 2 -> 3 -> 4，我们应当返回新列表 2 -> 1 -> 4 -> 3 的头节点。
思路：
递归

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def jh(self, l1:ListNode):
        head=l1
        head,head.next =head.next,head
        while not head:
            head.next=self.jh(head.next.next)
        return l1

