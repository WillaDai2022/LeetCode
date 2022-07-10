# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.max_sum = float("-inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0
            
            # 如果值小于0则直接舍弃
            left_max = max(0, dfs(root.left))
            right_max = max(0, dfs(root.right))
            
            curr_max = root.val + left_max + right_max
            
            self.max_sum = max(self.max_sum, curr_max)
            return root.val + max(left_max, right_max)
        
        dfs(root)
        
        return self.max_sum