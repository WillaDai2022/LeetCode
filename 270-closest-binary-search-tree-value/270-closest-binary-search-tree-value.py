# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return false
        node_queue = collections.deque([root])
        min = abs(target - root.val)
        res = root.val
        
        while node_queue:
            curr = node_queue.popleft()
            if abs(target - curr.val) < min:
                min = abs(target - curr.val)
                res = curr.val
                
            
            if curr.left:
                node_queue.append(curr.left)
                
            if curr.right:
                node_queue.append(curr.right)
        
        return res