class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t or abs(len(s) - len(t)) > 1:
            return False
        
        left_s, left_t = 0,0
        
        while left_s < len(s) and left_t < len(t):
            if s[left_s] == t[left_t]:
                left_s += 1
                left_t += 1
            else:
                break
                
        if left_s == len(s) or left_t == len(t):
            return True
        
        if len(s) == len(t):
            return s[left_s + 1:] == t[left_t + 1:] 
        elif len(s) < len(t):
            return t[left_t] + s[left_s:] == t[left_t:]
        else:
            return s[left_s] + t[left_t:] == s[left_s:]