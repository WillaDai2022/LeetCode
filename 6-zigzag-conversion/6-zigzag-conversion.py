class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        
        index = 0
        flag = -1
        res = [""]*numRows
        
        for c in s:
            res[index] += c
            if index == 0 or index == numRows - 1:
                flag = -flag
            index += flag
        
        return "".join(res)
            
