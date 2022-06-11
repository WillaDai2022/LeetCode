class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
       
        rooms = 0
        
        starts = []
        ends = []
        
        for start, end in intervals:
            starts.append(start)
            ends.append(end)
            
        starts.sort()
        ends.sort()
   
        
        p1, p2 = 0,0
        
        count = 0
        while p1 < len(starts):
            if starts[p1] < ends[p2]:
                count += 1
                p1 += 1
                rooms = max(rooms, count)
            else:
                count -= 1
                p2 += 1
                
        return rooms
                