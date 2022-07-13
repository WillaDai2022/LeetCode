class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        res = []
        
        def backtracking(n, k, start_idx):
            
            if len(path) == k:
                res.append(path[:])
                return
            
            #剪枝优化
            for i in range(start_idx, n-(k-len(path))+2):
                path.append(i)
                backtracking(n,k,i+1)
                path.pop()
                
        backtracking(n,k,1)
        return res