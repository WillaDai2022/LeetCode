class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        
        if n < 4:
            return []
        
        if n == 4:
            
            if sum(nums) == target:
                return [nums,]
            else:
                return []
            
        res = []
        nums.sort()
            
        for i in range(n - 3):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            if sum(nums[i:i + 4]) > target:
                break
                
            if nums[i] + sum(nums[-3:]) < target:
                continue
            
                
            for j in range(i + 1, n - 2):
                
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                if nums[i] + sum(nums[j: j + 3]) > target:
                    break
                    
                if nums[i] + nums[j] + sum(nums[-2:]) < target:
                    continue
                
                #2 pointers
                left = j + 1
                right = n - 1

                while left < right:

                    sum_4 = nums[i] + nums[j] + nums[left] + nums[right]

                    if sum_4 == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1


                    elif sum_4 > target:
                        right -= 1

                    else:
                        left += 1
                   
        return res                