from Class1 import ListNode

class Solution:
    def addTwoNumbers(self,l1,l2):
        head1=l2
        head2=l2
        l3=ListNode()
        cur = l3
        cur.val=0
        while head1 and head2:
            sum = head1+head2
            re2=0
            if sum>10:
                re1 = sum%10
                re2 = sum-10
            else:
                re1=sum
            cur.val += re1
            cur = cur.next
            cur.val = re2
            head1 =head1.next
            head2= head2.next
        cur = head1 if head1 else head2
        return cur


