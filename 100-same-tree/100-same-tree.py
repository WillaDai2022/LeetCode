# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        queue1 = deque([p])
        queue2 = deque([q])
        
        while queue1 and queue2:
            curr1 = queue1.popleft()
            curr2 = queue2.popleft()
            
            if curr1.val != curr2.val:
                return False
            
            if curr1.left and curr2.left:
                queue1.append(curr1.left)
                queue2.append(curr2.left)
            elif curr1.left or curr2.left:
                return False
                
            if curr1.right and curr2.right:
                queue1.append(curr1.right)
                queue2.append(curr2.right)
            elif curr1.right or curr2.right:
                return False
                
        return True
            