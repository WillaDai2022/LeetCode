# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorder(root, [])
    
    def postorder(self, root, a_list):
        if not root:
            return a_list
        
        self.postorder(root.left, a_list)
        self.postorder(root.right, a_list)
        a_list.append(root.val)
        
        
        return a_list