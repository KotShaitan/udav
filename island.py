class Solution:
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        def dfs(i, j):
            grid[i][j] = 0
            
            neib = [
                (i-1, j-1), (i-1, j), (i-1, j+ 1),
                (i, j-1),             (i, j+ 1),
                (i+1, j-1), (i+1, j), (i+1, j+ 1),
            ]   
            neib = [
                k
                for k in neib
                if 0 <= k[0] < n and 0 <= k[1] < m
            ]
            for i1, j1 in neib:
                if grid[i1][j1]:
                    dfs(i1, j1)
                
        
            
        ans = 0 
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    ans += 1
                    dfs(i, j)
        return ans