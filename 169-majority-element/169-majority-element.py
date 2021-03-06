class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        num = nums[0]
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] == num:
                count += 1
            else:
                count -= 1
                
            if count == 0:
                num = nums[i + 1]
                
        return num