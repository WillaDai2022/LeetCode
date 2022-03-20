class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        #dictionary storing all the symbols
        dict1 = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        res = 0
        len_s = len(s)
     
        
        for i in range(len_s - 1):
            if dict1[s[i]] < dict1[s[i+1]]:
                res -= dict1[s[i]]
            if dict1[s[i]] >= dict1[s[i+1]]:
                res += dict1[s[i]]
        res += dict1[s[len_s - 1]]
                
        return res