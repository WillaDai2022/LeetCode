class Solution:
    def countPrimes(self, n: int) -> int:
        
        count = 0
        
        primes = [True]*n
        scope = int(math.sqrt(n))
        
        for i in range(2, scope + 1):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
                    
        for i in range(2, n):
            if primes[i]:
                count += 1
                
        return count
                    