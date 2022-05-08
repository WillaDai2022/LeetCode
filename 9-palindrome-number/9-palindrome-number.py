class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        
        while s:
            if s[0] == s[-1]:
                s = s[1: len(s) - 1]
            else:
                return False
            
        return True