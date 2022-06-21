class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_left = height[0]
        max_right = height[-1]
        res = 0
        
        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                res += max_left-height[left] # This will never be negative
            else:
                right -= 1
                max_right = max(max_right, height[right])
                res += max_right-height[right] # This will never be negative
                
        return res