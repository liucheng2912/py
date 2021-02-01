# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    #def extend(self,l1,l2):
    #    l1 = ListNode()
     #   l2 = ListNode()
     #   for i in l2:
      #      l1.next=i

    def mergeTwoLists(self, l1:ListNode, l2:ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #做个伪节点
        res=ListNode(0)
        #l3指向伪节点
        l3=res
        while l1 and l2:
                if l1.val<l2.val:
                    l3.next=l1
                    l1=l1.next
                else:
                    l3.next=l2
                    l2=l2.next
                l3=l3.next
        l3.next=l1 or l2
        #不要伪节点
        return l3.next

if __name__ =='__main__':
    a=Solution()
    print(a.mergeTwoLists('[1,2,4]','[1,3,4]'))



