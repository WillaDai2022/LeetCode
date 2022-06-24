# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
       
        stack = []
        res = []
        visited = set()
       
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                visited.add(curr)
                curr = curr.left
            else:
                curr = stack[-1]
                if not curr.right or curr.right in visited:
                    res.append(stack.pop().val)
                    curr = None
                else:
                    curr = curr.right
                
        return res
            