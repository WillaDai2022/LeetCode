class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self.helper(s,t) and self.helper(t,s)
        
        
    def helper(self, s, t):
        dic = {}
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] != t[i]:
                return False
            
            dic[s[i]] = t[i]
            
        return True