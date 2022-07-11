# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 1
        
        def dfs(root, curr_val, count):
            nonlocal res
            if not root:
                return
            
            if root.val == curr_val:
                count += 1
                res = max(res, count)
                dfs(root.left, curr_val + 1, count)
                dfs(root.right, curr_val + 1, count)
            else:
                dfs(root.left, root.val + 1, 1)
                dfs(root.right, root.val + 1, 1)
            
            
        dfs(root, root.val + 1, 1)
        return res