class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set() 
        res = 0
        def dfs(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == 1): 
                return 0
            
            if r == ROWS - 1 and c == COLS - 1: 
                return 1

            visit.add((r,c))
            uniquePaths = 0
            uniquePaths += dfs(r + 1, c)
            uniquePaths += dfs(r - 1, c)
            uniquePaths += dfs(r, c - 1)
            uniquePaths += dfs(r, c + 1)

            visit.remove((r, c))
            return uniquePaths

        return dfs(0, 0)

        
        



        