class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        #nums[-1] = nums[n] = -∞ 意味着数组两个边界都是下坡
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            middle = (left + right)//2
            
            if nums[middle] > nums[middle + 1]:
                right = middle
            else:
                left = middle + 1
                
        return right