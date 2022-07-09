# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        
        queue = deque([root])
        height = 0
        
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
                    

            if height % 2 == 1:
                level.reverse()
      
                
            res.append(level)
            height += 1
            
        return res