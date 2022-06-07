class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 2
        
        for i in range(2,len(nums)):
            if nums[i] != nums[left-2]:
                nums[left] = nums[i]
                left += 1
                
        return left
                