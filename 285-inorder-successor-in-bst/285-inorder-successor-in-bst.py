# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        stack = []
        found = False
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
        
            root = stack.pop()
            if found:
                return root
            if root == p:
                found = True
            root = root.right
            