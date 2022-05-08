class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.findStart(nums, target)
        right = self.findEnd(nums, target)
        
        return [left, right]
    
    
    def findStart(self,nums,target):
        
        index = -1
        left, right = 0, len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                    index = middle

            if nums[middle] >= target:
                right = middle - 1
            else:
                left = middle + 1
            
        return index
    
    def findEnd(self, nums, target):
        
        index= -1
        left, right = 0, len(nums) -1
        
        while left <= right:
            middle = (left + right) // 2 
            
            if nums[middle] == target:
                index = middle
                
            if nums[middle] <= target:
                left = middle + 1
            else:
                right = middle - 1
                
        return index
            
            