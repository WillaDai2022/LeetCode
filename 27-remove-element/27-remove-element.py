class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        low = 0
        
        for num in nums:
            if num != val:
                nums[low] = num
                low += 1
        
        return low