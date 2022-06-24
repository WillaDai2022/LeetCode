# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        from collections import deque
        
        queue = deque([root])
        
        res = []
        while queue:
            l = []
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                l.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                    
                if curr.right:
                    queue.append(curr.right)
                    
            res.append(l)
        res.reverse()
        return res