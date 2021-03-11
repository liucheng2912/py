
class DListNode:
    def __init__(self,x=0,y=0):
        self.key=x
        self.val=y
        self.pre=None
        self.next=None

class Solution:
    def __init__(self):
        self.head=DListNode()
        self.tail=DListNode()
        self.head.next=self.tail
        self.tail.pre=self.head
        self.cache=dict()

    def get(self,key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_end(node)
        return node.val

    def set(self,key,value,k):
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self.move_to_end(node)
        else:
            node=DListNode(key,value)
            self.cache[key]=node
            self.add_to_end(node)
            if len(self.cache)>k:
                removed= self.head.next
                self.remove(removed)
                del self.cache[removed.key]
    def remove(self,node):
        node.pre.next=node.next
        node.next.pre=node.pre

    def add_to_end(self,node):
        node.pre=self.tail.pre
        node.next=self.tail
        self.tail.pre.next=node
        self.tail.pre=node