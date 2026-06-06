# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        first = head
        sec = head

        for i in range(n):
            first =  first.next
            # print(i,first.val)
        if not first:
            return head.next
        
        while first.next:
            first = first.next
            sec = sec.next
        print(sec.val)
        sec.next = sec.next.next

        return head



                


        