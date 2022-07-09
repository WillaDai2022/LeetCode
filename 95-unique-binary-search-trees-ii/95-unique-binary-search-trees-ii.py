# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generateTrees(start, end):
            if start > end:
                return [None]
            
            all_trees = []
            
            for node in range(start, end + 1):
                
                left = generateTrees(start, node-1)
                right = generateTrees(node+1, end)
                
                for l in left:
                    for r in right:
                        root = TreeNode(node)
                        root.left = l
                        root.right = r
                        all_trees.append(root)
                        
            return all_trees
        return generateTrees(1,n)
                
        
        