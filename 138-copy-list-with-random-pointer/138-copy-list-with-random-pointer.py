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
        if not head:
            return head
        
        old_copy = {}
        
        curr = head
        
        while curr:
            copy = Node(curr.val)
            old_copy[curr] = copy
            curr = curr.next
            
        curr = head
        while curr:
            copy = old_copy[curr]
            copy.next = old_copy[curr.next] if curr.next else None
            copy.random = old_copy[curr.random] if curr.random else None
            curr = curr.next
        
        return old_copy[head]