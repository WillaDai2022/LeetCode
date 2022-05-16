# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.preorder(root, [])
    
    def preorder(self, root, a_list):
        if not root:
            return []
        
        a_list.append(root.val)
        self.preorder(root.left, a_list)
        self.preorder(root.right, a_list)
        
        return a_list
    
    