class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.v = vec
        self.r = 0
        self.c = 0

    def next(self) -> int:
        while self.r < len(self.v) and self.c == len(self.v[self.r]):
            self.r += 1
            self.c = 0
        value = self.v[self.r][self.c]
        self.c += 1
        return value
        

    def hasNext(self) -> bool:
        while self.r < len(self.v) and self.c == len(self.v[self.r]):
            self.r += 1
            self.c = 0
            
        return self.r < len(self.v)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()