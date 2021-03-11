from Class1 import ListNode

class Solution:
    def reverse1(self,head):
        pre=None
        cur=head
        while cur:
            tmp=cur.next
            cur.next=pre
            pre=cur
            cur=tmp
        return cur
    