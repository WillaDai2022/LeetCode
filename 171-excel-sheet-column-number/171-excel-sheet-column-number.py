class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        
        while columnTitle:
            curr = columnTitle[0]
            num = num*26 + (ord(curr) + 1 - ord('A'))
            columnTitle = columnTitle[1:]
            
        return num