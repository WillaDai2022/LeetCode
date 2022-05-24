# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = list()
        
        if not root:
            return paths

        node_queue = collections.deque([root])
        path_queue = collections.deque([str(root.val)])
        
        while node_queue:
            curr = node_queue.popleft()
            path = path_queue.popleft()
            
            if not curr.left and not curr.right:
                paths.append(path)
            
            if curr.left:
                node_queue.append(curr.left)
                path_queue.append(path + "->" + str(curr.left.val))
                
            if curr.right:
                node_queue.append(curr.right)
                path_queue.append(path + "->" + str(curr.right.val))
        
       
        return paths
        
        
        