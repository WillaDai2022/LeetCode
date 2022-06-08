class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini = len(nums) + 1
        total = 0
        low = 0
        
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                mini = min(mini, i-low + 1)
                total -= nums[low]
                low += 1
                        
        return 0 if mini == len(nums) + 1 else mini
        
                