class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}
        
        curr = 1
        res = 0
        
        for char in s[::-1]:
            if dict1[char] >= curr:
                res += dict1[char]
            else:
                res -= dict1[char]
            curr =  dict1[char]
                
        return res