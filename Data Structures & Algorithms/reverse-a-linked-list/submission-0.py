# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        self.prev  = None
        self.current = head
        self.new = head.next 

        while self.current is not None:
            self.new = self.current.next
            self.current.next = self.prev
            self.prev = self.current
            self.current = self.new 
            head = self.prev
        else:
            return head

        

  
            

        
        
        