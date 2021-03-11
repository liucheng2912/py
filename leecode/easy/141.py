'''
思路：
    快慢指针
'''
from Class1 import ListNode
class Solution:
    def hasCycle(self,head):
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False
