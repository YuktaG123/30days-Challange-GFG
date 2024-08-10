class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def rotate(self, head, k):
        last = head
        sz = 1
        while last.next:
            last = last.next
            sz+=1
        if k==sz:
            return head
        
        pev = None
        curr = head
        while k:
            pev = curr
            curr = curr.next
            k-=1
        
        pev.next = None
        last.next = head
        return curr
