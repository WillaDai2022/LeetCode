class Solution:
    def addBinary(self, a: str, b: str) -> str:
    
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0

            total = digit_a + digit_b + carry
            curr = total % 2
            carry = total // 2 

            res = str(curr) + res

        if carry > 0:
            res = "1" + res

        return res
