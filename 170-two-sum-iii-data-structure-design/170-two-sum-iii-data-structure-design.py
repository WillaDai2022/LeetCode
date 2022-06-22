class TwoSum:

    def __init__(self):
        self.container = []

    def add(self, number: int) -> None:
        self.container.append(number)
        self.container.sort()

    def find(self, value: int) -> bool:
        left = 0
        right = len(self.container) -1
        
        while left < right:
            if self.container[left] + self.container[right] == value:
                return True
            
            if self.container[left] + self.container[right] < value:
                left += 1
            else:
                right -= 1
                
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)