# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #创建一个头结点 l1，然后使用一个指针用来指向l1，next指向head
        # cur用来寻找重复的元素，找到重复的元素时，phead就保持不动，直到cur找到不重复的元素时
        l1=ListNode(-1)
        phead=l1
        phead.next=head
        cur=head
        while cur and cur.next:
            if cur.val!=cur.next.val:
                cur=cur.next
                phead=phead.next
            else:
                val=cur.val
                while cur and val==cur.val:
                    cur=cur.next
                phead.next=cur
        return head.next


if __name__=='__main__':
    a=Solution()
    n=[1,2,3,3,4,4,5]
    m=ListNode(n)
    print(m.val)
    b=a.deleteDuplicates(m)
    print(b)






