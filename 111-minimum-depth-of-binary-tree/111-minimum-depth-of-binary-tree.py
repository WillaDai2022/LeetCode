# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = []
        queue.append(root)
        depth = 0
        
        while queue:
            size = len(queue)
            depth += 1
           
            while size:
                curr = queue.pop(0)
                size -= 1
                if not curr.left and not curr.right:
                    return depth
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
            
            
                    
 