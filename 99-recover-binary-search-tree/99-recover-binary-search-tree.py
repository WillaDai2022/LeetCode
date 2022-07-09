# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
            
        inorder(root)
     
        node1 = None
        node2 = None
        pre = nodes[0]
        for i in range(1,len(nodes)):
            if pre.val > nodes[i].val:
                node2 = nodes[i]
                if not node1:
                    node1 = pre
            pre =  nodes[i]
            
        if node1 and node2:
            node1.val, node2.val = node2.val, node1.val

