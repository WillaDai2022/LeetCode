class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        queue = collections.deque()
        
        left, right = 0, 0
        
        #Maintain a decending monotonic queue
        while right < len(nums):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)
            
            #left if out of bound
            if left > queue[0]:
                queue.popleft()
            
            if right - left + 1 == k:
                res.append(nums[queue[0]])
                left += 1
            right += 1
            
        return res