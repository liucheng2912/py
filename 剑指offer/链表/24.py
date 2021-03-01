'''
    思路：
        链表 head head.next
        只要将head.next的next指向head就行
        直到head.next为none
        需要用一个值来存储head.next.next
        1->2->3->4
        None<-1<-2 3->4
'''
from Class1 import ListNode
class Solution:
    def reverseList(self,head):
        pre=None
        cur=head
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre