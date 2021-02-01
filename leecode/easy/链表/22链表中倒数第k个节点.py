'''
输出链表的倒数第k位的链表
快慢指针的方法
p2先走k步，当p2到最后的时候，p1现在的内容就是倒数k的链表
'''
def order(head,k):
    p1=head
    p2=head
    for i in range(k):
        p1=p1.next
    while p1:
        p1=p1.next
        p2=p2.next
    return p2
