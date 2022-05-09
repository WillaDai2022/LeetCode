class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        
        while s[-1] == " ":
            s = s[0: len(s) - 1]
        for i in range(len(s)- 1, -1, -1):
            if s[i] != " ":
                length += 1
            else:
                break
                
        return length