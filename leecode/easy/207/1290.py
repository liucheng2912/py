from Class1 import ListNode
def f(head):
    cur=head
    temp=0
    while cur:
        temp+=cur.val*2
        cur=cur.next