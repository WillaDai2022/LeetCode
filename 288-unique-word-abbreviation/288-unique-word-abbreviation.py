class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dic = collections.defaultdict(set)
        
        for word in dictionary:
            if len(word) < 3:
                continue
            key = self.get_abbriv(word)
            self.dic[key].add(word)
        

    def isUnique(self, word: str) -> bool:
        if len(word) < 3:
            return True
        elif self.get_abbriv(word) not in self.dic:
            return True
        elif self.dic[self.get_abbriv(word)] == {word}:
            return True
        else:
            return False
    
    def get_abbriv(self, word):
        return word[0] + str(len(word[1:-1])) + word[-1] 
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)