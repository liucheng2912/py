'''
思路：
    找出单向链表中倒数第k个节点，返回该节点的值
    两个指针，一个指针先向前走k步，到末尾，head到需要的节点
'''
from Class1 import ListNode

class Solution:
    def f(self,head,k):
        p=head
        for i in range(k):
            p=p.next
        while p.next !=None:
            head=head.next
            p=p.next
        return head.val