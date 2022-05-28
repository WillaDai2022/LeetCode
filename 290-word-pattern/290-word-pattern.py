class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = s.split()
        
        if len(s) != len(pattern):
            return False
        
        dic = {}
        values = set()
        
        for i in range(len(s)):
            if pattern[i] in dic and dic[pattern[i]] != s[i]:
                return False
            if pattern[i] not in dic and s[i] in values:
                return False
            if pattern[i] not in dic:
                dic[pattern[i]] = s[i]
                values.add(s[i])
        return True