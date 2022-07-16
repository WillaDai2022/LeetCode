# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(nums, l, r):
            if l > r:
                return None
            
            middle = (l+r)//2
            root = TreeNode(nums[middle])
            
            root.left = helper(nums,l,middle-1)
            root.right = helper(nums, middle + 1, r)
            
            return root
        
        return helper(nums, 0, len(nums)-1)