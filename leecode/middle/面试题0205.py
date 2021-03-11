'''
思路：
链表val相加 然后将值取余保存到链表中，假如next为None 但是有进项，则新建一个节点
'''
from Class1 import ListNode
class Solution:
    def addTwoNumbers(self,l1,l2):
        res=ListNode(-1)
        cur=res
        emp=0
        while l1 and l2:
            s= l1.val+l2.val+emp
            l1.val=s%10
            emp=s//10
            cur.next=l1
            cur=cur.next
            l1,l2=l1.next,l2.next
        left=l1 if l1 else l2
        while left and emp>=0:
            s=left.val+emp
            left.val=s%10
            emp=s//10
            cur.next=left
            cur=cur.next
            left=left.next
        if emp>0:
            cur.next=ListNode(emp)
        return res.next

