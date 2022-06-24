# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        
        def helper(root, height):
            if not root:
                return
            
            if len(res) == height:
                res.append([])
                
            res[height].append(root.val)
            helper(root.left, height + 1)
            helper(root.right, height + 1)
            
        helper(root,0)
        return res