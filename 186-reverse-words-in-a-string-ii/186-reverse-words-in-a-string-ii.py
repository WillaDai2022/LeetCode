class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s, left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                
        reverse(s, 0 , len(s)-1)
        
        left = right = 0
        
        while right < len(s):
            while right < len(s) and s[right] != " ":
                right += 1
            
            reverse(s, left, right-1)
            
            right += 1
            left = right