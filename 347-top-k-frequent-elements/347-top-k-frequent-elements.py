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
                
    
        #找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        res = [0] * k
        for i in range(k-1, -1, -1):
            res[i] = heapq.heappop(pri_queue)[1]
            
        return res