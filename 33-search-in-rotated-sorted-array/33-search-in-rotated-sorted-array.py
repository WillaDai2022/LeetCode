class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。此时有序部分用二分法查找。无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环. 
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right)//2
            
            if target == nums[middle]:
                return middle
            
            #left sorted portion
            if nums[left] <= nums[middle]:
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
                    
            #right sorted portion
            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1
                    
        return -1
        