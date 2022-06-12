from collections import deque

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = deque(v1)
        self.v2 = deque(v2)
        self.v1_flag = True

    def next(self) -> int:
        if self.v1_flag:
            if self.v1:
                value = self.v1.popleft()
                self.v1_flag = False
            else:
                value = self.v2.popleft()
        else:
            if self.v2:
                value = self.v2.popleft()
                self.v1_flag = True
            else:
                value = self.v1.popleft()
            
        return value 
    
    def hasNext(self) -> bool:
        return len(self.v1) + len(self.v2) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())