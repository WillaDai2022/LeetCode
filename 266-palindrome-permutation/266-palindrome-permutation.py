class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_dict = {}
        
        for c in s:
            if c not in char_dict:
                char_dict[c] = 1
            else:
                del char_dict[c]
                
        return len(char_dict) <= 1
            