class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
       
        matrix = [[0]*n for _ in range(n)]
  
        left, right, top, bottom = 0, n -1, 0, n - 1
        start = 1
        end = n*n
        
        while start <= end:
            
            for i in range(left, right + 1):
                matrix[top][i] = start
                start += 1
            
            top += 1
            
            for i in range(top, bottom + 1):
                matrix[i][right] = start
                start += 1
                
            right -= 1
            
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = start
                start += 1
                
            bottom -= 1
            
            for i in range(bottom, top-1, -1):
                matrix[i][left] = start
                start += 1
                
            left += 1
            
        return matrix