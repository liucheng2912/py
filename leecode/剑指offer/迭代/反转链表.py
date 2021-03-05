"""
思路：
链表的head.next 指向 head 此时 head变为head.next head.next变为head

tmp=head
1->2->3->4->5-Null
head,head.next=head.next,head
tmp=head.next
2->1->3->4->5->Null
head.next,head.next.next=head.next.next,head.next
tmp,tmp.next=tmp.next,tmp
tmp=tmp.next
2->3->1->4->5->Null
head.next.next,head.next.next.next=head.next.next.next,head.next.next
tmp,tmp.next=tmp.next,tmp
tmp=tmp.next
2->3->4->1->5->Null
head.next.next.next,head.next.next.next.next=head.next.next.next.next,head.next.next.next
tmp,tmp.next=tmp.next,tmp
tmp=tmp.next
2->3->4->5->1->Null
head.next.next.next.next.next=Null
tmp.next=null

tmp=head
2->3->4->5->1->Null
tmp,tmp.next=tmp.next,tmp
tmp=head.next
3->2->4->5->1-Null
tmp,tmp.next=tmp.next,tmp
tmp=head.next
3->4->2->5->1-Null
tmp,tmp.next=tmp.next,tmp
tmp=head.next
3->4->5->2->1-Null
if tmp.val>tmp.next.val or tmp.next is Null:
    结束循环

思路：
将当前节点的next指针改为指向前一个节点，
首先存储当前的next节点,以防丢失 temp=cur.next
然后next指向pre cur.next=pre
再将pre指针后移 pre=cur
再将cur指针后移 cur=temp
最后引用新的头引用 return pre
pre=null
curr=head
if curr !=null
    pre,cur=cur,pre
    cur=cur.next

"""
from Class1 import ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
      pre=None
      cur=head
      while cur:
          temp=cur.next
          cur.next=pre
          pre=cur
          cur=temp
      return pre
