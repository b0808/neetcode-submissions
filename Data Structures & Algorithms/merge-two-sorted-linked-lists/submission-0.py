# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        if list1 is None:
            return list1
        
        self.list1 = list1
        self.list2 = list2
        self.head = ListNode()
        self.current = self.head
        while self.list2 and self.list1 :
            if self.list2.val >= self.list1.val:
                self.current.next = self.list1
                self.current  = self.list1
                self.list1= self.list1.next
                
            else:
                self.current.next = self.list2
                self.current  = self.list2
                self.list2 = self.list2.next
        
        self.current.next = self.list1 or self.list2
        return self.head.next
            
        