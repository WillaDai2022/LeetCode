class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = collections.defaultdict(set) # all the numbers in this col
        rows = collections.defaultdict(set) # all the numbers in this row
        squares = collections.defaultdict(set) # all the numbers in a 3*3 square, key = (row//3, col//3)
        
        for r in range(9):
            for c in range(9):
                
                #ignore empty cell
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in cols[c] 
                    or board[r][c] in rows[r]
                    or board[r][c] in squares[(r//3, c//3)]):
                    
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
                
        return True