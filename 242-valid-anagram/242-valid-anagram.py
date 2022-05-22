class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        dict1 = {}
        
        for c in s:
            dict1[c] = dict1.get(c,0) + 1
            
        for c in t:
            dict1[c] = dict1.get(c,0) - 1
            if dict1[c] < 0:
                return False
            
        return True