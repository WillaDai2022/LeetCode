class Solution:
    def countPrimes(self, n: int) -> int:
        # 埃氏筛
        prime = [True]*n
        count = 0
        
        for i in range(2, int(math.sqrt(n))+1):
            if prime[i]:
                for j in range(i*i, n, i):
                    prime[j] = False
        
        for i in range(2,n):
            if prime[i]:
                count += 1
                
        return count