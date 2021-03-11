'''
思路：
    首先判断是否有环
    假如有环的话 在他们相遇的节点
    将fast置为head 然后相遇的节点为入环的第一个节点
'''
from Class1 import ListNode

class Solution:
    def detectCycle(self,head):
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                fast=head
                while fast!=slow:
                    fast=fast.next
                    slow=slow.next
        return None
