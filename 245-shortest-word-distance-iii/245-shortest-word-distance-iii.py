class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        p1, p2 = -1, -1
        min_dis = len(wordsDict)
        
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                p1 = i
                
            if wordsDict[i] == word2:
                if word1 == word2:
                    p1 = p2
                p2 = i
                
            if p1 != -1 and p2 != -1:
                min_dis = min(min_dis, abs(p1-p2))

        return min_dis