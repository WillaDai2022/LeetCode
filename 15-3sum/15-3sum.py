class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        if(len(nums) < 3):
            return result
        
        nums.sort()
        
        for index, n in enumerate(nums):
            if index >0 and n == nums[index - 1]:
                continue
            
            left = index +1
            right = len(nums) - 1
          
            while left < right:
                three_sum = n + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else: 
                    result.append([n, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        
        return result