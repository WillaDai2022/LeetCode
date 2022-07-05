# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        path = []
        paths = []
        
        def dfs(root,targetSum):
            if not root:
                return
            path.append(root.val)
            
            if not root.left and not root.right and targetSum - root.val == 0:
                paths.append(path[:])

            dfs(root.left, targetSum-root.val)
            dfs(root.right, targetSum-root.val)
            path.pop()
        
        dfs(root, targetSum)
        return paths