'''
思路：
将该节点变为他的下一个节点
node.val=node.next.val
node.next=node.next.next
'''
from Class1 import ListNode

class Solution(object):
    def de1(self,node):
        node.val=node.next.val
        node.next=node.next.next
