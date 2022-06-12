from collections import deque

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        #The function reversed() returns an iterator, not an actual list. You cannot directly get the len() of an iterator
        self.v1 = list(reversed(v1))
        self.v2 = list(reversed(v2))
        self.v1_flag = True

    def next(self) -> int:
        if self.v1_flag:
            if self.v1:
                value = self.v1.pop()
                self.v1_flag = False
            else:
                value = self.v2.pop()
        else:
            if self.v2:
                value = self.v2.pop()
                self.v1_flag = True
            else:
                value = self.v1.pop()
            
        return value 
    
    def hasNext(self) -> bool:
        return len(self.v1) + len(self.v2) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())