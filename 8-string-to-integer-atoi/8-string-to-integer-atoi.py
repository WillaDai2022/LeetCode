class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
       
        res_list = re.findall(r"^[\+\-]?\d+", s) #r"^[-|+]?\d+"
        
        #findall 返回一个列表,*用于unpack
        num = int(*res_list)
        
        return min(max(num, -2**31), 2**31-1)