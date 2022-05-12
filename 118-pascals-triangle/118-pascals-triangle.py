class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]] #First row
        
        
        for i in range(numRows - 1):
            temp = [0] + res[i] + [0] #0 at the start and end of each row
            row = []
            
            for j in range(len(res[-1])+1):
                row.append(temp[j] + temp[j+1])
                
            res.append(row)
        
        return res