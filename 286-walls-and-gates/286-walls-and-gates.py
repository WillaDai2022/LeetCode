class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        #bfs solution
        
        rows = len(rooms)
        cols = len(rooms[0])
        queue = collections.deque()
        
        def add_room(r, c, dis):
            if (0 <= r < rows and
                0 <= c < cols and
                rooms[r][c] == 2147483647):
                
                rooms[r][c] = dis
                queue.append((r,c))
            else:
                return
        
        
        #add all the gates in the queue
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c))
        
        dist = 1
        while queue:
            #bfs
            for i in range(len(queue)):
                r, c = queue.popleft()
            
                add_room(r-1, c, dist)
                add_room(r+1, c, dist)
                add_room(r, c-1, dist)
                add_room(r, c+1, dist)
                
            dist +=  1
                
            
            
            
            
                