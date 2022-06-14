class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])
        
        #给格子周围除了格子本身值加10
        def add_10(row,col):
            for r in [row-1, row, row+1]:
                for c in [col-1, col, col+1]:
                    if r < 0 or r >= rows or c < 0 or c >= cols or(r == row and c == col):
                        continue
                    board[r][c] += 10
                    
        #遍历格子，如果数字取模10为1， 则其周围格子都增加10
        for row in range(rows):
            for col in range(cols):
                if board[row][col] % 10 == 1:
                    add_10(row, col)
                    
        for row in range(rows):
            for col in range(cols):
                if board[row][col]%10 == 1 and (board[row][col] // 10 == 2 or board[row][col] // 10 == 3):
                    board[row][col] = 1
                elif board[row][col]%10 == 0 and (board[row][col] // 10 == 3):
                    board[row][col] = 1
                else:
                    board[row][col] = 0