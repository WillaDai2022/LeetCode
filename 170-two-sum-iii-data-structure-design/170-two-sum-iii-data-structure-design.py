class TwoSum:

    def __init__(self):
        self.container = {}

    def add(self, number: int) -> None:
        self.container[number] = self.container.get(number, 0) + 1
        
    def find(self, value: int) -> bool:
        for key in self.container:
            comp = value - key
            if (comp == key and self.container[key] >= 2) or (comp != key and comp in self.container):
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)