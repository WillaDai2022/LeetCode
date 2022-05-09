class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1
        
        if nums[-1] < target:
            res = len(nums) - 1
        
        while left <= right:
            
            middle = (left + right) //2 
            
            if nums[middle] == target:
                return middle
                
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
                
        return left
            