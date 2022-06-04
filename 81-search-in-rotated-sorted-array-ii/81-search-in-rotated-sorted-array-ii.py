class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            
            middle = (left + right) // 2
            
            if nums[middle] == target:
                return True
            
            if nums[left] == nums[middle] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[middle]:
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1
                    
        return False