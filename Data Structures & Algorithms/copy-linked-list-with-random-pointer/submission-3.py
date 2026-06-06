"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        new_node = None
        dict_1 = {}
        dict_random = {}
        dict_next = {}
        i = 0

        if head is None:
            return None

        while current is not None:
                new_node = Node(current.val,None,None)
                dict_1[current] = new_node
                current = current.next
                i = i+1

        
        current = head
        new_node = None
        while current is not None:
            if current == head:
                new_node = dict_1[current]
                if current.next:
                    new_node.next = dict_1[current.next]
                else:
                    new_node.next = None

                if current.random:
                    new_node.random = dict_1[current.random]
                else:
                    new_node.random = None
                current = current.next
                new_head = new_node
            else:
                new_node = dict_1[current]
                if current.next:
                    new_node.next = dict_1[current.next]
                else:
                    new_node.next = None

                if current.random:
                    new_node.random = dict_1[current.random]
                else:
                    new_node.random = None
                current = current.next

        return new_head




                

            




            
        
        


        