'''
思路：
生成一个新的链表
然后遍历两个链表
'''
from Class1 import ListNode
class Solution:
    def mergeTwoLists(self,l1,l2):
        l3=ListNode(0)
        p1=l1
        p2=l2
        p3=l3
        while p1 and p2:
            if p1.val<p2.val:
                p3.next,p1=p1,p1.next
            else:
                p3.next,p2=p2,p2.next
            p3=p3.next
        p3.next= p1 if p1 else p2
        return l3.next
