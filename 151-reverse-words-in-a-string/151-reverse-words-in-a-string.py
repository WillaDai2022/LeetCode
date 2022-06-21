class Solution:
    def reverseWords(self, s: str) -> str:
        
        left, right = 0, len(s)-1
        
        #remove the white space
        while s[left] == " ":
            left += 1
            
        while s[right] == " ":
            right -= 1
            
        res = ""
        
        while left <= right:
            index = right
            while index >= left and s[index] != " ":
                index -= 1
                
            res += s[index + 1 : right + 1]
            
            if index > left:
                res += " "
            
            while s[index] == " ":
                index -= 1
                
            right = index
        
        return res