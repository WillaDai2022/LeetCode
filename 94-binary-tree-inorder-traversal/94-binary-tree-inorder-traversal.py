# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        queue = deque()
        res = []
        
        while queue or root:
            if root:
                queue.append(root)
                root = root.left
            else:
                root = queue.pop()
                res.append(root.val)
                root = root.right
                
        return res