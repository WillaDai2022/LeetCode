class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        x_reverse = 0
        
        while x > x_reverse:
            x_reverse = x_reverse * 10 + x % 10
            x = x // 10
            
        return x == x_reverse or x == x_reverse//10