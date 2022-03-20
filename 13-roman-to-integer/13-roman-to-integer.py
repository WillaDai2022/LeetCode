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
        # current val equals the smallest value
        curr_val = 1
        res = 0
        
        #loop numerals from end to start
        for char in s[::-1]:
            #if value represent by the numeral greater than or equals to current value
            if dict1[char] >= curr_val:
                #add the value to result
                res += dict1[char]
                #current value equals to the value represented by this numeral
                curr_val = dict1[char]
            else:
                #subtract from the result
                res -= dict1[char]
        return res