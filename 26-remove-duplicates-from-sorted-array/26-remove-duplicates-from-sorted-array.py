class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        low = 0
        
        for high in range(1, len(nums)):
            if nums[low] != nums[high]:
                low += 1
                nums[low] = nums[high]
        
        return low + 1