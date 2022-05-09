class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        l = 1
        r = x // 2
        
        while(l <= r):
            middle = (l + r) // 2
            if middle == x // middle:
                return middle
            elif middle > x // middle:
                r = middle - 1
            else:
                l = middle + 1 
                
        return l - 1