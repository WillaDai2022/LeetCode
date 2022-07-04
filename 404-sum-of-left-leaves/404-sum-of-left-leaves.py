# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 0
        stack = deque([root])
        
        while stack:
            curr = stack.pop()
            
            if curr.left and not curr.left.left and not curr.left.right:
                res += curr.left.val
                
            if curr.right:
                stack.append(curr.right)
                
            if curr.left:
                stack.append(curr.left)
                
    
        return res