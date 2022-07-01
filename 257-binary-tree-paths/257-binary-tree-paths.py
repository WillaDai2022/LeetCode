# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        if not root:
            return paths
        
        path = ""
        
        
        def preorder(node, path, paths):
            path += str(node.val)
            
            if not node.left and not node.right:
                paths.append(path)
    
            
            if node.left:
                preorder(node.left, path + "->", paths)
            
            if node.right:
                preorder(node.right, path + "->", paths)
    
        preorder(root, path, paths)
        return paths
    
            
            