# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        nodes = []
        def preorder(node, nodes):
            if not node:
                nodes.append("N")
                return
            
            nodes.append(str(node.val))
            preorder(node.left, nodes)
            preorder(node.right, nodes)
        
        preorder(root, nodes)
        return ",".join(nodes)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        idx = 0
        
        def dfs():
            nonlocal idx
            if vals[idx] == "N":
                idx += 1
                return None
            
            root = TreeNode(int(vals[idx]))
            idx += 1
            root.left = dfs()
            root.right = dfs()
            
            return root
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))