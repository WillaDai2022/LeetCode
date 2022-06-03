class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        start = 0
        end = m*n - 1
        
        while start <= end:
            middle = (start + end)//2
            
            if matrix[middle//n][middle%n] == target:
                return True
            elif matrix[middle//n][middle%n] < target:
                start = middle + 1
            else:
                end = middle - 1
                
        return False
            
            