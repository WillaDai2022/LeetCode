# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        
        if not root:
            return paths
        
        
        node_q = deque([root])
        path_q = deque([str(root.val)])
        
        while node_q:
            node = node_q.popleft()
            path = path_q.popleft()
            
            if not node.left and not node.right:
                paths.append(path)
                
            if node.left:
                node_q.append(node.left)
                l_path = path + "->" + str(node.left.val)
                path_q.append(l_path)
                
            if node.right:
                node_q.append(node.right)
                r_path = path + "->" + str(node.right.val)
                path_q.append(r_path)
                
        return paths
            
            