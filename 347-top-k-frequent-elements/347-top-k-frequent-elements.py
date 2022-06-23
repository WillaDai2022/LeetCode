import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        
        #calculate the frequency of each number
        for num in nums:
            dic[num] = dic.get(num,0) + 1
            
        pri_queue = []
        
        for num, freq in dic.items():
            heapq.heappush(pri_queue, (freq, num))
            if len(pri_queue) > k:
                heapq.heappop(pri_queue)
                
        res = []
        #in any order
        for i in range(len(pri_queue)-1, -1, -1):
            res.append(pri_queue.pop()[1])
            
        return res