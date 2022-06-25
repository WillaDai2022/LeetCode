# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        left_num = self.countNodes(root.left)
        right_num = self.countNodes(root.right)
        
        num = left_num + right_num + 1
        
        return num