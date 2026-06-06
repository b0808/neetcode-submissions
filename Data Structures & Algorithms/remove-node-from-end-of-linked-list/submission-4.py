# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        first = head
        sec = head

        # Move first pointer n steps ahead
        for _ in range(n):
            first = first.next

        # If first is None, it means we remove the head
        if not first:
            return head.next

        # Move both until first reaches the last node
        while first.next:
            first = first.next
            sec = sec.next

        # Remove the nth node from end
        sec.next = sec.next.next

        return head



                


        