class Solution:
    def jump(self, nums: List[int]) -> int:
        
        res = 0
        
        #left, right points
        left,right = 0,0
        farest = 0 
        
        while right < len(nums)-1:
   
            for i in range(left, right + 1):
                farest = max(farest, i+nums[i])
            left = right + 1
            right = farest
            res += 1
        return res
                
                