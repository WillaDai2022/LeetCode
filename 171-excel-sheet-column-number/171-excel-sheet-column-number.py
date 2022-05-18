class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        
        for i in range(len(columnTitle)):
            c = columnTitle[i]
            num = num*26 + ord(c) + 1 - ord('A')
    
        return num