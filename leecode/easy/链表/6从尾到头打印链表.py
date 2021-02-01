# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # 栈
    # 时间、空间复杂度O(n)
    def reversePrint(self, head):
        stack=[]
        plist=[]
        while head:
            stack.append(head.val)
            head=head.next
        while stack:
            plist.append(stack.pop())
        return plist
    #递归实现
    #时间控件复杂度都为O(n)
    def reversePrint1(self, head):
        plist=[]
        if head is None:
            return []
        plist=self.reversePrint1(head.next)
        plist.append(head.val)
        return plist
