class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] != t[i]:
                return False
            elif t[i] in dic.values() and s[i] not in dic:
                return False
            
            dic[s[i]] = t[i]
            
        return True