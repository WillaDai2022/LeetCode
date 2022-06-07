class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        def dfs(r,c):
            if not 0 <= r < rows or not 0 <= c <cols or grid[r][c] == "0":
                return
            
            grid[r][c] = '0'
            
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count += 1
                    
        return count