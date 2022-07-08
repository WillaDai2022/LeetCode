class Solution:
    def numTrees(self, n: int) -> int:
        
        # dp[0] = 1 # 0 node
        # dp[1] = 1 # 1 node
        dp = [1] * (n+1)
        
        for nodes in range(2, n+1): #number of nodes
            total = 0
            for root in range(1, nodes+1): # node 1 as root, node 2 as root...
                left = root - 1
                right = nodes - root
                total += dp[left] * dp[right]
            dp[nodes] = total
            
        return dp[n]
            