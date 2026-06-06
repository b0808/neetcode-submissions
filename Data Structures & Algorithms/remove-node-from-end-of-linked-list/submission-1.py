# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head is None:
            return None
        prev = None
        curr = head
        N = 0
        m = 0
        curr2 = head
        while curr2 is not None:
            m = m+1
            curr2 = curr2.next

        k = m-n
        print(m,n,k)
        while curr is not None:

            if k == 0:
                return head.next

            
            if N ==k:
                if not head.next:
                    return None
                if curr.next and prev.next:
                    prev.next = curr.next
                else:
                    prev.next = None
                return head
            else:
                temp = curr.next
                prev = curr
                curr = temp 
                N = N+1
        return head


                


        