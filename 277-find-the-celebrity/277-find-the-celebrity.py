# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0
        
        #find the potential celebrity
        for i in range(1,n):
            if knows(celebrity, i):
                celebrity = i
                
        #confirm it's the celebrity
        for i in range(n):
            if (i != celebrity and knows(celebrity, i)) or not knows(i, celebrity):
                return -1
            
        return celebrity