import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #桶排序
        
        dic = {}
        
        #calculate the frequency of each number
        for num in nums:
            dic[num] = dic.get(num,0) + 1
        
        #index stands for the frequency and the inner list stores the nums 
        bucket = [[] for _ in range(len(nums)+1)]
        
        for num, freq in dic.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
                