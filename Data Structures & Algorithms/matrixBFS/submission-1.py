from collections import deque 
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0, -1), (-1, 0)]
        queue = deque()
        visit = set() 

        queue.append((0,0))
        visit.add((0,0))
        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1: 
                    return length
                
                for dy, dx in directions: 
                    new_x = dx + c 
                    new_y = dy + r 

                    if (min(new_x, new_y) < 0) or new_y == ROWS or new_x == COLS or grid[new_y][new_x] == 1 or (new_y, new_x) in visit:
                        continue 
                    
                    queue.append((new_y, new_x))
                    visit.add((new_y, new_x))
            length += 1
        
        return -1
