from Class1 import ListNode
class Solution:
    def removeNthFromEnd(self,head,n):
        p3=ListNode()
        p1,p2=head,head
        for _ in range(n):
            p2=p2.next
        while p2:
            p3.next=p1
            p1,p2=p1.next,p2.next
        if p1==head:return head.next
        p3.next=p1.next
        return head
