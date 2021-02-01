class ListNode(object):
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution(object):
    def deleteNode(self,head,val):
        head1=ListNode(0)#创建假头
        head1.next=head#指向head
        #构建双指针
        p1=head1
        p2=head1.next
        while True:
            if p2.val==val:
                #若值找到，p1的next指向p2的next
                p1.next= p2.next
            else:
                #若没找到，则继续向后找
                p1=p1.next
                p2=p2.next
        return head