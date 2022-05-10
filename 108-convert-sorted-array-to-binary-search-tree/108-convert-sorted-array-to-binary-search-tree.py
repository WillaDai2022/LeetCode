# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums, start, end):
            if start > end:
                return None
            
            middle = (start + end) // 2
            
            root = TreeNode(nums[middle])
            
            root.left = helper(nums, start, middle - 1)
            root.right = helper(nums, middle + 1, end)
            return root
        
        return helper(nums, 0, len(nums) - 1)