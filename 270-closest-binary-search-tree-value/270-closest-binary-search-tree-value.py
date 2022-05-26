# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:    
        self.min = abs(target - root.val)
        self.val = root.val
        
        def rec(node):
            if not node: 
                return False
            if abs(node.val - target) < self.min:
                self.min = abs(node.val - target)
                self.val = node.val
            rec(node.left)
            rec(node.right)
            
        rec(root)
        return self.val