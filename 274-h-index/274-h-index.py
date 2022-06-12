class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        
        citations.sort()
        count = 1
        
        for i in range(len(citations)-1, -1, -1):
            if citations[i] >= count:
                count += 1
                
        return count-1