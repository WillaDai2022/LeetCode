# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_depth = 1
        
        def dfs(node, curr_depth):
            nonlocal max_depth
            if not node:
                max_depth = max(max_depth, curr_depth-1)
                return 
            
            dfs(node.left, curr_depth + 1)
            dfs(node.right, curr_depth + 1)
            
        dfs(root, 1)
        return max_depth
            