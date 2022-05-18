class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
       
        while columnNumber:
            # 26进制题目的加一变形,减一则变为普通26进制
            columnNumber -= 1
            res = chr(columnNumber%26 + ord('A')) + res
            columnNumber //= 26
        
        return res