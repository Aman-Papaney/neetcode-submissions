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
        nodes = {}

        curr = head
        
        while curr:
            temp = Node(curr.val)
            nodes[curr] = temp
            curr = curr.next
            
        curr = head
        dummy = Node(x = 0)
        temp = dummy
        
        while curr:
            nodes[curr].next = nodes.get(curr.next)
            nodes[curr].random = nodes.get(curr.random)
            temp.next = nodes[curr]
            curr = curr.next
            temp = temp.next
        
        return dummy.next
