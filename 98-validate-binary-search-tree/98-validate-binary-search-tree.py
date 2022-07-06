# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        #方法三，中序遍历迭代
        
        queue = []
        pre = None
        
        while queue or root:
            while root:
                queue.append(root)
                root = root.left
                
            root = queue.pop()
            
            if pre == None:
                pre = root.val
            else:
                #中序遍历为升序
                if pre >= root.val:
                    return False
                pre = root.val
            root = root.right
            
        return True  
      
        