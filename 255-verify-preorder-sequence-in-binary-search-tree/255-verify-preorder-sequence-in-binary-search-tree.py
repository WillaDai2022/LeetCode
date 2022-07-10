class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        
        stack = []
        min_pop = float("-inf")
        
        for val in preorder:
            if val < min_pop:
                return False
            
            while stack and val > stack[-1]:
                min_pop = stack.pop()
                
            
            stack.append(val)
            
        
        return True
                
            