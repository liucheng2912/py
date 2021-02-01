class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def mergeTwoLists(self,l1,l2):
        # 若l1或l2有一方为空，则无需合并直接返回即可
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val<l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2

