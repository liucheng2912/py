class ListNode(object):
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution(object):
    def reverseList(self,head):
        #三指针实现翻转，通过cur将读取的加在pre的头部
        if not head or not head.next:return head
        pre,cur,next=None,head,head,next
        while cur.next is not None:
            cur.next=pre
            pre=cur
            cur=next
            next=cur.next
        cur.next=pre
        return head