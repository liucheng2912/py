"""
反转一个单链表。
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
思路：
递归实现

结束条件
只有一个节点 直接返回
两个节点，交换位置
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pass