# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        nodes = deque([root])
        sums = deque([targetSum])
        
        while nodes:
            curr_node = nodes.pop()
            curr_sum = sums.pop()
            
            if not curr_node.left and not curr_node.right and curr_sum - curr_node.val == 0:
                return True
            
            if curr_node.right:
                nodes.append(curr_node.right)
                sums.append(curr_sum - curr_node.val)
                
            if curr_node.left:
                nodes.append(curr_node.left)
                sums.append(curr_sum - curr_node.val)
                
        return False