class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for index in range(len(nums)):
            if nums[index] == 0:
                nums.remove(nums[index])
                nums.append(0)
            
  
            