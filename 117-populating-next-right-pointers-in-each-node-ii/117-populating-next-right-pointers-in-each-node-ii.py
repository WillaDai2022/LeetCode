"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        curr = root
        head = None
        connect = None
        
        while curr:
            while curr:
                if curr.left:
                    if head == None:
                        head = curr.left
                        connect = curr.left
                    else:
                        connect.next = curr.left
                        connect = connect.next
                
                if curr.right:
                    if head == None:
                        head = curr.right
                        connect = curr.right
                    else:
                        connect.next = curr.right
                        connect = connect.next
                curr = curr.next
                
            curr = head
            head = None
            connect = None
            
        return root
                