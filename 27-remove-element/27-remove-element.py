class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        low = 0
        
        for high in range(0, len(nums)):
            
            if nums[high] != val:
                nums[low] = nums[high]
                low += 1
        
        return low