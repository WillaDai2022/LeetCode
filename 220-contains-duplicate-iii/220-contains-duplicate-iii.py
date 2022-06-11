from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        window = SortedList()
        
        for idx, n in enumerate(nums):
            if idx > k:
                window.remove(nums[idx -1 -k])
                
            pos1 = bisect_left(window, n-t)
            pos2 = bisect_right(window, n+t)
            
            if pos1 != pos2:
                return True
              
            window.add(n)
    
        return False