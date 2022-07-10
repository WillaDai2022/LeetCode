# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node or not node.left:
                return node        
   
            new_node = dfs(node.left) #node now is the parent of new_node
            node.left.left = node.right
            node.left.right = node
            node.left = node.right = None
            
            return new_node
        
        return dfs(root)