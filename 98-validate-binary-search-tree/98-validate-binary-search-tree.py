# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        #bst的定义是左边节点值均小于节点，右边均大于
        #注意陷阱，左边不仅小于其直接父母，也小于其爷爷，曾祖。。。
        #left随着树向下不断变小，right则随着树向下不断增大
        
        def isBST(node, left, right):
            
            if not node:
                return True
            
            if not(left < node.val < right):
                return False
            
            return isBST(node.left, left, node.val) and isBST(node.right, node.val, right)
        
        return isBST(root, float("-inf"), float("inf"))