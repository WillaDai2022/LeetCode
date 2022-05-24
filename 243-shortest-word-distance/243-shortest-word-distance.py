class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        index1 = -1
        index2 = -1
        res = len(wordsDict)
        
        for i, w in enumerate(wordsDict):
            if w == word1:
                index1 = i
                if index2 >= 0:
                    res = min(res,abs(index1 - index2))
                    
            if w == word2:
                index2 = i
                if index1 >= 0:
                    res = min(res, abs(index1 - index2))
                    
        return res