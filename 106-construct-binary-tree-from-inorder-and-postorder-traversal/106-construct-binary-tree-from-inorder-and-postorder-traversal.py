# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not inorder and not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        
        in_index = inorder.index(postorder[-1])
        
        root.left = self.buildTree(inorder[:in_index], postorder[:in_index])
        
        root.right = self.buildTree(inorder[in_index+1:], postorder[in_index:-1])
        
        return root