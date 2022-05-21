class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        index = 0
        
        while index < len(nums):
            curr_index = index
            while index + 1< len(nums) and nums[index] == nums[index+1]-1:
                index += 1
                
            if curr_index != index:
                s = str(nums[curr_index]) + "->" + str(nums[index])
            else:
                s = str(nums[index])
            
            res.append(s)
            index += 1
           
        return res