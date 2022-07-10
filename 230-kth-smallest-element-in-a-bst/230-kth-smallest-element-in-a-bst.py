# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:    
        _k = k
        res = 0
        
        def inorder(root):
            nonlocal _k
            nonlocal res
            if not root:
                return
         
            inorder(root.left)
            _k -= 1
            if _k == 0:
                res = root.val
            inorder(root.right)
        
        inorder(root)
        return res