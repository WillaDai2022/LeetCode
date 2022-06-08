class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0
       
        
        def bfs(r, c):
            queue = collections.deque()
            queue.append((r,c))
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            
            while queue:
                row, col = queue.popleft()
                for d1, d2 in directions:
                    r = d1 + row
                    c = d2 + col
                    if (0 <= r < rows and 
                        0 <= c < cols and 
                        grid[r][c] == "1"):
                        queue.append((r, c))
                        grid[r][c] = "0"
                
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    bfs(r, c)
                    count += 1
                    
        return count