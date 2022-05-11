# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        nodeStack = [root]
        sumStack =[targetSum - root.val]
        
        while nodeStack:
            curr = nodeStack.pop()
            sum = sumStack.pop()
            
            if not curr.left and not curr.right and sum == 0:
                return True
            
            if curr.left:
                nodeStack.append(curr.left)
                sumStack.append(sum - curr.left.val)
                
            if curr.right:
                nodeStack.append(curr.right)
                sumStack.append(sum - curr.right.val)
                
        return False
            
        