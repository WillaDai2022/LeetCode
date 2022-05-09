# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
         return self.dfs(root, [])
        
    def dfs(self, node, list_1):
        if not node:
            return list_1
        
        self.dfs(node.left, list_1)
        list_1.append(node.val)
        self.dfs(node.right, list_1)
        
        return list_1
        
        
        