# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = float("-inf")
        
        def dfs(root):
            nonlocal max_sum
            if not root:
                return 0
            
            # 如果值小于0则直接舍弃
            left_max = max(0, dfs(root.left))
            right_max = max(0, dfs(root.right))
            
            curr_max = root.val + left_max + right_max
            
            max_sum = max(max_sum, curr_max)
            return root.val + max(left_max, right_max)
        
        dfs(root)
        
        return max_sum