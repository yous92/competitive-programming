class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        memo = [[-1]*n for _ in range(m)]
        
        def dp(i,j):
            if i >= m or j >= n:
                return float('inf')
            if i == m-1 and j == n-1:
                return grid[i][j]
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            down = dp(i+1,j)
            right = dp(i,j+1)
            
            memo[i][j] = grid[i][j]+ min(down,right )
            return memo[i][j]
        
        return dp(0,0)