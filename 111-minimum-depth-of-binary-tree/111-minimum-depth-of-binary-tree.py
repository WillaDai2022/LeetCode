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
        
        from collections import deque
        
        queue = deque([root])
        res = 0
        
        while queue:
            size = len(queue)
            res += 1
            
            for _ in range(size):
                curr = queue.popleft()

                if not curr.left and not curr.right:
                    return res

                if curr.left:
                    queue.append(curr.left)
                
                
                if curr.right:
                    queue.append(curr.right)
                

 