"""思路：
假设链表其余部分已经反转，节点k+1到n已经反转，正处于k 则希望k+1的next指向k 即n.next.next=n
特殊节点1必须指向None
"""
from Class1 import ListNode
def f(head:ListNode):
    if (head==None or head.next==None):return head
    n=f(head.next)
    head.next.next=head
    head.next=None
    return n
