class WordDistance:

    def __init__(self, wordsDict: List[str]):
        
        self.d = collections.defaultdict(list)
        
        for index, word in enumerate(wordsDict):
            self.d[word].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        l1 = self.d.get(word1)
        l2 = self.d.get(word2)
        
        p1 = 0
        p2 = 0
        
        min_dis = float('inf')
        
        while p1 < len(l1) and p2 < len(l2):
            min_dis = min(min_dis, abs(l1[p1]-l2[p2]))
            
            if l1[p1] > l2[p2]:
                p2 += 1
            else:
                p1 += 1
        
        return min_dis

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)