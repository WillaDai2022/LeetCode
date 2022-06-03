class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        if target < matrix[0][0] or target > matrix[rows-1][cols-1]:
            return False
        
        i = 0
        while target > matrix[i][cols - 1]:
                i  += 1
                
        if target < matrix[i][0]:
            return False
        
        for j in range(cols):
            if matrix[i][j] == target:
                return True
            
        return False