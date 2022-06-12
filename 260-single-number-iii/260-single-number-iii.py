class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        temp = 0
        
        #这一步可以得到只出现一次的n1, n2
        #结果为n1^n2
        for num in nums:
            temp ^= num
        
        #n&(-n) 的结果为最末尾的一个1，其余置零
        #因为n1 != n2, 必然两个数其中至少一位结果不同，一个为1一个为0
        bit = temp & (-temp)
        
        res = [0,0]
        
        for num in nums:
            #该位为1的数
            if bit & num == 0:
                res[0] ^= num
            else:
                res[1] ^= num
                
        return res
                
            