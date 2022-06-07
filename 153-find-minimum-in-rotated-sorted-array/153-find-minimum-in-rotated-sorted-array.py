class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        mini = nums[0]
        
        while left <= right:
            
            if nums[left] < nums[right]:
                return min(mini, nums[left])
            
            middle = (left + right)//2
            
            mini = min(mini, nums[middle])
            
            if nums[left] <= nums[middle]:
                left = middle + 1
            else:
                right = middle
                
        return mini
            
            