class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        low = 0
        
        for num in nums:
            if num != nums[low]:
                low += 1
                nums[low] = num
                
        return low+1