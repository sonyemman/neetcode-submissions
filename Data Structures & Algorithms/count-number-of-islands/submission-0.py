class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        s = set() 
        ROWS,COLS = len(grid), len(grid[0])
        numIsland = 0
        visited = set()
        

        def dfs(r, c, visited): 
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0" or (r,c) in visited: 
                return 
            
            visited.add((r,c))

            for dx, dy in directions: 
                newX, newY = dx + r, dy + c 
                dfs(newX, newY, visited)
        

        for i in range(ROWS): 
            for j in range(COLS): 
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j, visited)
                    numIsland += 1
        return numIsland

            


        