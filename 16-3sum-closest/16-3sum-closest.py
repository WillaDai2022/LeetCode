class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        min_sum = 100000
        nums.sort()
        
        
        for index, n in enumerate(nums):
            
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            
            left = index + 1
            right = len(nums) - 1
            
            while left < right:
            
                sum = n + nums[left] + nums[right]
                
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(target-min_sum):
                    min_sum = sum

                elif sum > target:
                    right -= 1
                    
                else:
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return min_sum