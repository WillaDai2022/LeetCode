class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        res = [1]*(rowIndex + 1)
        
        for i in range(1,rowIndex):
#Remember that you're overwriting the current index with *the value in the current index plus the value in the index to the left of it*. If you go left to right, you change the value in the current index and move to the right, but when you try to base it off of the index to the left of it (as mentioned above), that ends up being the index you just changed. Going right to left ensures you're not taking into account any numbers you just changed. Try going left to right and using a rowIndex of 3. You get [1, 3, 4, 1] instead of [1, 3, 3, 1] because of this.

            for j in range(i, 0, -1):
                res[j] = res[j] + res[j-1]
                
        return res             
        
        