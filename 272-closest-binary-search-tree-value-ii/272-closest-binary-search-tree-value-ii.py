# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        
        def helper(node, target, heap):
            if not node:
                return
            
            heapq.heappush(heap, (abs(target-node.val), node.val))
            helper(node.left, target, heap)
            helper(node.right, target, heap)
            
        res = []
        heap = []
        helper(root, target, heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
            
        return res
        
        