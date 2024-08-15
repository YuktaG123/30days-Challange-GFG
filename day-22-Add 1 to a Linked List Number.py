class Solution:
    def reverseList(self, head):
        temp, prev = head, None
        
        while temp != None:
            nextt = temp.next
            temp.next = prev
            prev = temp
            temp = nextt
        
        return prev
            
    def addOne(self,head):
        revHead = self.reverseList(head)
        
        temp, carry = revHead, 1
        newHead, curr = None, None
        
        while temp != None:
            currVal = temp.data + carry
            carry = currVal // 10
            if newHead == None:
                newHead = Node(currVal % 10)
                curr = newHead
            else:
                curr.next = Node(currVal % 10)
                curr = curr.next
            
            temp = temp.next
            
        if carry > 0:
            curr.next = Node(carry)
        
        return self.reverseList(newHead)
