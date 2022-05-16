class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        
        #a ^a = 0 a^0 = a
        for num in nums:
            res ^= num
            
        return res