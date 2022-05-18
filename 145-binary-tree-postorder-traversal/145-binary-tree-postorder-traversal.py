# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        res = []
        visited = set()
        
        while root or stack:
            while root:
                stack.append(root)
                visited.add(root)
                root = root.left
            
            root = stack[-1]
            
            if not root.right or root.right in visited:
                res.append(stack.pop().val)
                root = None
            else:
                root = root.right
                 
        return res
            
            