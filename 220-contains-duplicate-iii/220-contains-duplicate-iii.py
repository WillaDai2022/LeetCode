from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        window = SortedList()
        
        for idx, n in enumerate(nums):
            if idx > k:
                window.remove(nums[idx -1 -k])
            
            #如果n-t比window[-1]大，那么n+t肯定也比window[-1]大，则pos1 = pos2 = len(window) - 1
            #如果n+t比window[0]小，那么n-t肯定也比window[0]小，则pos1 = pos2 = 0
            #其余情况说明要么n-t比最小值大，要么n+t比最大值小或者同时
            pos1 = bisect_left(window, n-t)
            pos2 = bisect_right(window, n+t)
        
            if pos1 != pos2:
                return True
              
            window.add(n)
    
        return False