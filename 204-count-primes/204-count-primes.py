class Solution:
    def countPrimes(self, n: int) -> int:
        
        count = 0
        
        primes = [True]*n
        scope = int(math.sqrt(n))
        
        # 从 2 开始枚举到 sqrt(n)。
        for i in range(2, scope + 1):
            # 如果当前是素数
            if primes[i]:
                # 就把从 i*i 开始，i 的所有倍数都设置为 false
                for j in range(i*i, n, i):
                    primes[j] = False
                    
        for i in range(2, n):
            if primes[i]:
                count += 1
                
        return count
                    