class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        
        for c in s:
            dict1[c] = dict1.get(c,0) + 1
            
        for c in t:
            dict1[c] = dict1.get(c,0) - 1
            if dict1[c] < 0:
                return False
            
        for i in dict1.values():
            if i != 0:
                return False
            
        
        return True