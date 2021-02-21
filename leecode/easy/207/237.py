'''
思路：
删除链表 将当前节点变为下一个节点
'''
from Class1 import ListNode
class Solution:
    def deleteNone(self,node):
        node.val=node.next.val
        node.next=node.next.next
