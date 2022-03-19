class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        #x is negative or x ends with 0 but is not 0 (e.g. 10 100 1000...)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        x_reverse = 0
        while x > x_reverse:
            #get the reversed x
            x_reverse = x_reverse*10 + x%10
            # remove the last digit of x each time
            x //= 10
            
        return x ==  x_reverse or x == x_reverse // 10
        