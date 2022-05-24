# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.dfs(root, [], "")

    
    
    def dfs(self, node, paths, path):
        if node:
            path += str(node.val)
            if not node.left and not node.right:
                paths.append(path)
            else:
                path += "->"
                self.dfs(node.left, paths, path)
                self.dfs(node.right, paths, path)
                
        return paths

        
       
        
        
        
        