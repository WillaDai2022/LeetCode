class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
      
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        
        copy = [[board[r][c] for c in range(cols)] for r in range(rows)]
        
        for row in range(rows):
            for col in range(cols):
                
                live_num = 0
                
                for neighbour in neighbors:
                    r = row + neighbour[0]
                    c = col + neighbour[1]
                    
                    if 0 <= r < rows and 0 <= c < cols and copy[r][c] == 1:
                        live_num += 1
                    
                if copy[row][col] == 1 and (live_num < 2 or live_num > 3):
                    board[row][col] = 0
                if copy[row][col] == 0 and live_num == 3:
                    board[row][col] = 1