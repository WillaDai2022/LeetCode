class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        #[i][j] after rotation is [j][n -1 - i]
        #[j][n - 1 - i] after roration is [n-1 -i][n - 1 - j]
        #[n-1 -i][n - 1 - j] after roration is [n - i - j][i]
        #[n - i - j][i] after roration is [i][j]
        
        #We change 4 points at once. If n is even, we should make n^2 / 4 = (n/2)(n/2) changes and if n is odd, we should make (n^2-1) / 4 = ((n-1)/2) ((n+1)/2) times because we dont move the center
        
        for i in range(n // 2):
            for j in range((n+1) //2):
                temp = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = temp
            
        
        
        
        
        

        
        #https://leetcode.cn/problems/rotate-image/solution/xuan-zhuan-tu-xiang-by-leetcode-solution-vu3m/