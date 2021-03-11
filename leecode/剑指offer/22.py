'''
双指针
slow slow+k
'''
from Class1 import ListNode
class Solution:
    def getKthFromEnd(self,head,k):
        p1=head
        p2=head
        for i in range(k):
            p2=p2.next
        while p2:
            p1=p1.next
            p2=p2.next
        return p1