class Solution:
    def maxArea(self, height: List[int]) -> int:
        start_point = 0
        end_point = len(height)-1
        max_area = 0
        
        while start_point < end_point:
            if height[start_point] < height[end_point]:
                max_area = max(max_area, (end_point-start_point)*height[start_point])
                start_point += 1
            else:
                max_area = max(max_area, (end_point-start_point)*height[end_point])
                end_point -= 1           
                
        return max_area