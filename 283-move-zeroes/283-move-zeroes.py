class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = 0
        
        for high in range(len(nums)):
            if nums[high] != 0:
                nums[high], nums[low] = nums[low], nums[high]
                low += 1
                
            
  
            