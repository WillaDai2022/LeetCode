# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        #方法二，将二叉树按照中序遍历转化为数组
        #bst中序遍历应该得到一个升序数组
      
        nodes_val = []
        
        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)
            nodes_val.append(node.val)
            inorder(node.right)
            
        def isValid(nodes):
            for i in range(1,len(nodes)):
                if nodes[i] <= nodes[i-1]:
                    return False
            return True
        
        inorder(root)
        return isValid(nodes_val)